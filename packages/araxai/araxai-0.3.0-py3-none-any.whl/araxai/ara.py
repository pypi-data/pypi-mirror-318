#0.0.51 auto boundaries
#56 - ability to order variables by importance
#57 - fixing bug - categories with both positive and negative value in chart
#reason: preparation for joining categories - must be also ZOHLEDNENO in conditions and prints, now it prints and uses first value only, see ['value'] in program
#fully fixed (or maybe developed)
#58 - return list json from print_
#59 - fixed printing bug for non-string data types

#TODO - remove print debugs

from cleverminer import cleverminer

import pandas
import time
import os

from matplotlib import pyplot as plt
from pandas.core.dtypes.common import is_categorical_dtype


class ara:
    """
    Categorical Lift-based Association Rules Analysis.
    Suitable for data profiling (what influences the target and how) as well as XAI method for explaining the model by simplification (how the model estimates a target).
    """

    version_string = "0.3.0"
    max_depth = 2
    min_base = 20
    print_rules_on_the_fly = 0
    default_boundaries = [2,5,10]
    boundaries = [2, 5, 10]
    auto_boundaries = False
    min_rules=2
    max_rules=10
    max_iter=10
    init_stepping=2
    max_seq_len=3
    font_size_big = 40
    font_size_normal=30
    order_by_importance = False


    dir = None

    res={}

    stats={}

    start_time = None
    end_time = None

    clms=[]
    is_var_ordered ={}

    def __init__(self,df:pandas.DataFrame=None,target=None,target_class=None,options=None,CL=None):
        """
        Categorical Lift-based Association Rules Analysis. Can be used for data / dependency profiling as well as XAI method for interpreting the model
        :param pandas.DataFrame df: pandas dataframe with input data
        :param string target: target variable of the dataset (profiling) or target prediction (for model explanation task)
        :param string target_class: target class of interest (when profiling more classes is needed, you can run this procedure in loop for all classes)
        :param dict options: dictionary with options. Valid options are max_depth (maximum depth of rules searched; default=2), min_base (minimum base of the rule searched, default 20), print_rules_on_the_fly (default 0), order_by_importance (default False)
        """
        if not(target in df.columns):
            print(f"Error: target variable ({target}) is not in dataframe.")
            exit(1)
        if not(target_class in df[target].unique()):
            print(f"Error: target class {target_class} is not present in ({target}) variable.")
            exit(1)
        if not(options is None):
            if "auto_boundaries" in options:
                ara.auto_boundaries = options.get("auto_boundaries")
            if "order_by_importance" in options:
                ara.order_by_importance = options.get("order_by_importance")
        if not(ara.auto_boundaries):
            self.res = self._arar(df=df,target=target,target_class=target_class,options=options,cond_CL=CL)
        else:
            self.res = self._arar_auto_boundaries(df=df,target=target,target_class=target_class,options=options,cond_CL=CL)

    @staticmethod
    def _arar_auto_boundaries(df: pandas.DataFrame = None, target=None, target_class=None, cond=None, cond_CL=None, clm=None, prepend_str='', depth=1, options=None, lift_pre=1):
        """
        internal procedure for the finding rule count that fits predefined range
        """
        need_change=1
        changes=0
        rules_iter=[]
        stepping=ara.init_stepping
        last_way=0
        bound=ara.default_boundaries

        opts =options
        opts['boundaries'] = bound


        while need_change==1 and changes<ara.max_iter:
            ara.res = ara._arar(df=df,target=target,target_class=target_class,options=opts)
            need_change=0
            changes+=1
            print(ara.res)
            rules = ara.res['results']["rules"]
            rules_iter.append(len(rules))
            if len(rules)<ara.min_rules:
                need_change=1
                if last_way==1:
                    stepping = (stepping-1)/2+1
                bound=[x/stepping for x in bound]
                last_way = -1
            if len(rules)>ara.max_rules:
                need_change=1
                bound=[x*stepping for x in bound]
                last_way=1
            opts['boundaries']=bound

        auto_boundaries={}
        auto_boundaries['changes']=changes
        auto_boundaries['rules_iter'] = rules_iter
        ara.res['task_info']['auto_boundaries']=auto_boundaries
        return ara.res


    @staticmethod
    def _arar(df: pandas.DataFrame = None, target=None, target_class=None, cond=None, cond_CL=None, clm=None, prepend_str='', depth=1, options=None, lift_pre=1,forced_boundaries=None):
        """
        internal procedure for the ara recursion
        """
#        print(f"...COND={cond}")
        cumlift=lift_pre
        if cond==None:
            ara.start_time=time.time()
            ara.stats={}
            ara.stats["clm_runs"]=0
            ara.stats["resulting_rules"]=0
            print(f"ARA version {ara.version_string}")
            if not(options is None):
                if type(options) is dict:
                    if "max_depth" in options:
                        ara.max_depth=options.get("max_depth")
                    if "min_base" in options:
                        ara.min_base = options.get("min_base")
                    if "print_rules_on_the_fly" in options:
                        ara.print_rules_on_the_fly = options.get("print_rules_on_the_fly")
                        print("WARNING: this option is marked as experimental. Will be replaced.")
                    if "font_size_big" in options:
                        ara.font_size_big = options.get("font_size_big")
                    if "font_size_normal" in options:
                        ara.font_size_normal = options.get("font_size_normal")
                    if "boundaries" in options:
                        if forced_boundaries is None:
                            b = options.get("boundaries")
                            if not(len(b)==3):
                                print("WARNING: boundaries parameter must have length of 3. Parameter will be ignored.")
                            else:
                                if b[0]<b[1] and b[1]<b[2]:
                                    ara.boundaries=b
                                else:
                                    print("WARNING: boundaries parameter must be ordered list. Parameter will be ignored.")
                        else:
                            print("WARNING: cannot combine boundaries and auto_boundaries. Boundaries arrtibute will be ignored.")

                else:
                    print("ERROR: options must be a dictionary")
                    return
            ara.clms = []
            for i in range(ara.max_depth):
                print(f"..will initialize CLM#{i+1}")
                clm_l=cleverminer(df=df)
                ara.clms.append(clm_l)
                for colname in df.columns:
                    is_ordered = False
                    if is_categorical_dtype(df[colname]):
                        if df[colname].cat.ordered:
                            is_ordered = True
                    ara.is_var_ordered[colname] = is_ordered
        res_ara = []
        if (df is None):
            print("Dataframe is missing")
            return
        if (target is None):
            print("Target is missing")
            return
        if not(target in df.columns):
            print(f"{target} is not present in the dataframe.")
            return
        def var_str_to_literal(name):
            d = {}
            d['name']=name
            d['minlen']=1
            is_ordered = ara.is_var_ordered[name]
            if is_ordered:
                d['type'] = 'seq'
                d['maxlen'] = ara.max_seq_len
            else:
                d['type']='subset'
                d['maxlen']=1
            return d
        an=[]
        def cond_str_lst(cond):
            res=[]
            if cond is None:
                return res
            attr= cond['attributes']
#            print(f"...attr :{attr}")
            for i in attr:
                res.append(i['name'])
            return res


        cCL=[]
        if cond_CL is not None:
            for cl in cond_CL:

                cCL.append(var_str_to_literal(cl))
        for nm in df.columns:
            if not(nm==target):
                if not(target in cond_str_lst(cond)):
                    an.append(var_str_to_literal(nm))
        su=[]
        if target_class is None:
            su.append(var_str_to_literal(target))
        else:
            d = {}
            d['name']=target
            d['type']='one'
            d['value']=target_class
            su.append(d)
        clm = ara.clms[depth-1]
        cnd = cond
        if cond is None:
            if cond_CL is None:
                clm.mine(proc='4ftMiner',quantifiers={'Base':ara.min_base}, ante ={'attributes':an, 'minlen':1, 'maxlen':1, 'type':'con'},
                   succ ={'attributes':su, 'minlen':1, 'maxlen':1 , 'type':'con'}
                         )
            else:
                clm.mine(proc='4ftMiner', quantifiers={'Base': ara.min_base},
                         ante={'attributes': an, 'minlen': 1, 'maxlen': 1, 'type': 'con'},
                         succ={'attributes': su, 'minlen': 1, 'maxlen': 1, 'type': 'con'},
                         cond = {'attributes': cCL, 'minlen': 1, 'maxlen': len(cCL), 'type': 'con'}
                         )
        else:
            clm.mine(proc='4ftMiner', quantifiers={'Base': ara.min_base},
                              ante={'attributes': an, 'minlen': 1, 'maxlen': 1, 'type': 'con'},
                              succ={'attributes': su, 'minlen': 1, 'maxlen': 1, 'type': 'con'},
                              cond = cond#_dic
                              )


#        clm.print_rulelist()

        ara.stats["clm_runs"] += 1


        if ara.order_by_importance:

            rulelist=[]
            for i in range(clm.get_rulecount()):
                rule = {}
                rule['id'] = i+1
                rule['lift'] = clm.get_quantifiers(i+1)['aad']+1
                rule['abslift'] = clm.get_quantifiers(i + 1)['aad']+1
                if rule['abslift']<1:
                    rule['abslift'] = 1/rule['abslift']
                rulelist.append(rule)

            rulelist = sorted(rulelist, key=lambda d: abs(d['abslift']))#, reverse=True)


        for ii in range(clm.get_rulecount()):
            if ara.order_by_importance:
                i = rulelist[ii]['id']-1
            else:
                i = ii
            rule_id = i+1
            fft = clm.get_fourfold(rule_id)
            lift = clm.get_quantifiers(rule_id)['aad']+1
            cumlift=lift_pre*lift
            valid = 0
            disp_str=""
            for i2 in range(len(ara.boundaries)):
                if lift > 1:
                    if lift>=ara.boundaries[i2]:
                        valid = i2 + 1
                        disp_str += "+"
                    else:
                        disp_str += "."
                elif lift < 1:
                    if lift <= 1/ara.boundaries[i2]:
                        valid = i2 - 1
                        disp_str += "-"
                    else:
                        disp_str += "."
                else:
                    disp_str="." * len(ara.boundaries)
            if not(valid==0):
                ara.stats["resulting_rules"] += 1
                ante_str = clm.result['rules'][i]['cedents_str']['ante']
                if ara.print_rules_on_the_fly==1:
                    if valid>0:
                        print(f"{prepend_str}{disp_str} {str(ante_str)} x{lift:.1f}")
                    else:
                        print(f"{prepend_str}{disp_str} {str(ante_str)} /{1/lift:.1f}")
                cs = clm.result['rules'][i]['cedents_struct']
                cl = cs['ante']
                cl.update(cs['cond'])

                cs2 = clm.result['rules'][i]['trace_cedent_dataorder']
                cl2 = cs2['ante'] + cs2['cond']
                cs2b = clm.result['rules'][i]['traces']
                vals2 = cs2b['ante'] + cs2b['cond']
                newcond=[]
                for i in range(len(cl2)):
                    ca = {}
                    ca['name'] = clm.result['datalabels']['varname'][cl2[i]]
                    #ca['value'] = clm.result['datalabels']['catnames'][cl2[i]][vals2[i][0]]
                    ca_values =[]
                    ca_values_str = ''
                    for ix in range(len(vals2[i])):
                        ca_values.append(clm.result['datalabels']['catnames'][cl2[i]][vals2[i][ix]])
                        ca_values_str += str(clm.result['datalabels']['catnames'][cl2[i]][vals2[i][ix]])
                        ca_values_str += ' '
                    ca_values_str = ca_values_str[:-1]
                    if len(vals2[i])==1:
                        ca['type'] = 'one'
                        ca['value'] = clm.result['datalabels']['catnames'][cl2[i]][vals2[i][0]]
                    else:
                        ca['type'] = 'list'
                        ca['value'] = ca_values
                    ca['values'] = ca_values
                    ca['values_str'] = ca_values_str
                    newcond.append(ca)
                cond_d = {}
                cond_d['attributes'] = newcond
                cond_d['minlen'] = len(cl.items())
                cond_d['maxlen'] = len(cl.items())
                cond_d['type'] = 'con'
                subres=[]
                if depth<ara.max_depth:
                    res_s=ara._arar(df,target=target,target_class=target_class,cond=cond_d,clm=clm,prepend_str='   ',depth=depth+1,lift_pre=cumlift)
                    subres = res_s
                res_l={}
                vars=[]
                for i in range(len(newcond)):
                    vr={}
                    vr['varname']=newcond[i]['name']
                    vr['values']=newcond[i]['values']
                    vr['values_str']=newcond[i]['values_str']
                    vars.append(vr)
                res_l['vars'] = vars
                res_l['fft'] = fft
                res_l['lift'] = lift
                res_l['cumlift'] = cumlift
                res_l["target_class_ratio"] = fft[0]/(fft[0]+fft[1])
                if lift > 1:
                    res_l['booster'] ='x' + "{:.1f}".format(lift)
                    res_l['booster_val'] = lift
                    res_l['booster_way'] = 'x'
                else:
                    res_l['booster'] ='/' + "{:.1f}".format(1/lift)
                    res_l['booster_val'] = 1/lift
                    res_l['booster_way'] = '/'
                res_l['valid_level'] = valid
                res_l['valid_level_disp_string'] = disp_str
                res_l['sub'] = subres
                res_ara.append(res_l)
#                clm.print_rule(rule_id)
#                print(f"...newcond{newcond}")
        if cond is not None:
            return res_ara
        profile = df.groupby([target])[target].count().to_dict()
        summ=0
        for k,v in profile.items():
            summ+=v
        tgt_ratio=profile[target_class]/summ
        res_total={}
        task_info={}
        task_info["target"]=target
        task_info["target_class"]=target_class
        opts={}
        opts["min_base"]=ara.min_base
        opts["max_depth"]=ara.max_depth
        task_info["opts"]=opts
        res_total["task_info"]=task_info
        ara.end_time = time.time()
        ara.stats["time_sec"] = ara.end_time-ara.start_time
        res_total["stats"]=ara.stats
        res_aa={}
        res_aa["target_var_profile"] = profile
        res_aa["target_class_ratio"] = tgt_ratio
        res_aa["rules"] = res_ara
        res_total["results"]=res_aa
        return res_total

    def get_task_info(self):
        """
        Gets a complete results in a machine readable form (dictionary)
        """
        return self.res

    def get_results(self):
        """
        Gets results in a machine readable form (dictionary)
        """
        if "results" in self.res:
            return self.res["results"]
        else:
            return {}

    def get_rules(self):
        """
        Gets a list of rules in a machine readable form (dictionary)
        """
        results = self.get_results()
        if "rules" in results:
            return results["rules"]
        else:
            return {}


    def print_result(self):
        """
        Prints the results into console
        """
        print("")
        print("ARA: VARIABLES THAT INFLUENCE TARGET CLASS SIGNIFICANTLY:")
        print("(+ increases occurrence, - decreases occurrence, more signs means stronger influence)")
        print("")
        rules = self.get_rules()
        return self._print_result(res_i=rules)
        print("")


    def _print_result(self,res_i=None,pre="",mult=1,depth=None):
        """
        internal procedure for the ara recursion
        """
        res=[]
        pre_cond=None
        pre_cond_last=None
        dpth=depth
        if dpth==None:
            dpth=1
        for item in res_i:
            res_this = {}
            total_lift = mult*item['lift']
            if total_lift>=1:
                total_lift_str="x" + "{:.1f}".format(total_lift)
            else:
                total_lift_str="/"+ "{:.1f}".format(1/total_lift)
            if len(item['vars'])>dpth:
                pre_cond = ""
                is_init=True
                cnt=0
                for iii in range(len(item['vars'])):
                    cnt+=1
                    if cnt>dpth:
                        s = str(item['vars'][cnt-1]['varname'])+'('+str(item['vars'][cnt-1]['values_str'])+')'
                        if is_init:
                            pre_cond = "CONDITION "+s
                            is_init=False
                        else:
                            pre_cond = pre_cond + " & "+s
                if not(pre_cond==pre_cond_last):
                    pre_cond_last=pre_cond
            print(f"{pre}{item['valid_level_disp_string']} {item['vars'][0]['varname']}({item['vars'][0]['values_str']}) {item['booster']} (={total_lift_str})")
            res_this['feature']=item['vars'][0]['varname'] +'(' + item['vars'][0]['values_str'] + ')'
            res_this['booster']=item['booster']
            res_this['booster_val']=item['booster_val']
            res_this['booster_way']=item['booster_way']
            if total_lift>=1:
                res_this['total_booster'] = total_lift_str
                res_this['total_booster_val'] = total_lift
                res_this['total_booster_way'] = 'x'
            else:
                res_this['total_booster'] = total_lift_str
                res_this['total_booster_val'] = 1/total_lift
                res_this['total_booster_way'] = '/'

            sub=[]
            if len(item['sub'])>0:
                sub = self._print_result(res_i=item['sub'],pre=pre+"    ",mult=total_lift,depth=dpth+1)
            res_this['sub'] = sub
            res.append(res_this)
        return res
    def _is_clara(self,res_i=None,depth=None):
        """
        internal procedure returning if the task was CL-ARA task
        """
        return self._is_clara_i(res_i=self.get_rules())

    def _is_clara_i(self,res_i=None,depth=None):
        """
        internal procedure returning if the task was CL-ARA task
        """
        res = False
        dpth=depth
        if dpth==None:
            dpth=1
        for item in res_i:
            if len(item['vars'])>dpth:
                pre_cond = ""
                is_init=True
                cnt=0
                for iii in range(len(item['vars'])):
                    cnt+=1
                    if cnt>dpth:
                        s = str(item['vars'][cnt-1]['varname'])+'('+str(item['vars'][cnt-1]['values_str'])+')'
                        if is_init:
                            pre_cond = "CONDITION "+s
                            is_init=False
                            res=True
#                        else:
#                            pre_cond = pre_cond + " & "+s
#                if not(pre_cond==pre_cond_last):
#                    pre_cond_last=pre_cond
#                    print(f"{pre_cond} : ")
#            print(f"{pre}{item['valid_level_disp_string']} {item['vars'][0]['varname']}({item['vars'][0]['value']}) {item['booster']} (={total_lift_str})")
            if len(item['sub'])>0:
                res = res or self._is_clara_i(res_i=item['sub'],depth=dpth+1)
        return res


    def print_task_info(self):
        """
        Prints the task info
        """
        if "task_info" in self.res:
            print("ARA: TASK SUMMARY:")
            tvar=self.res['task_info']['target']
            print(f"    Target variable      :{tvar}")
            tcl=self.res['task_info']['target_class']
            tcr=self.res['results']['target_class_ratio']
            print(f"    Target class         :{tcl} ({tcr:.2%})")
            tcp=self.res['results']['target_var_profile']
            print(f"    Target class profile :")
            for itm in tcp:
                print(f"                {str(itm).rjust(20,' ')} ({tcp[itm]:7d})")
            print("")
        else:
            print("Class not initialized. Please run ARA analysis first.")

    def print_statisics(self):
        """
        Prints task statistics
        """
        if "stats" in self.res:
            print("ARA: STATISTICS:")
            stats=self.res['stats']
            print(f"    Time needed       :{stats['time_sec']: .2f} seconds")
            print(f"    Cleverminer runs  :{stats['clm_runs']:3}")
            print(f"    Total rules found :{stats['resulting_rules']:3}")
        else:
            print("Class not initialized. Please run ARA analysis first.")

    def draw_result(self,dir=None):
        """
        Create charts for results into specified (or default) directory
        """
        if (self._is_clara()):
            print(f"Charts for CLARA are not implemented yet.")
            exit(1)
        print("")
        print("Preparing charts...")
        if not(dir==None):
            ara.dir=dir
        if ara.dir is None:
            ara.dir = os.getcwd()
            os.makedirs("fig", exist_ok=True)
            ara.dir = os.path.join(ara.dir, "fig")
        res=self.get_rules()
        #now, draw the chart with most significant influencers (literals/classes of variables that influence target category the most)
        x=[]
        y=[]
        y_loc=[]
        colr=[]
        colr_loc=[]
        x_grp=[]
        y_grp=[]
        colr_grp=[]
        for item in res:
            lbl = item['vars'][0]['varname']+"("+str(item['vars'][0]['values_str'])+")"
            val=item['lift']
            col='g'
            if val<1:
                val=-1/val
                col='r'
            x.append(lbl)
            y.append(val)
            colr.append(col)

        px = 1/plt.rcParams['figure.dpi']
        font = {'size'   : 8}

        plt.rc('font', **font)
        plt.figure(figsize=(1920*px,1080*px))
        plt.title("Overall dataset profiles/global model properties\n Lift of literals that most influence the target class",fontsize = ara.font_size_big)
        barlist=plt.barh(x,y)
        for i in range(len(colr)):
            barlist[i].set_color(colr[i])
        plt.tick_params(axis='y', labelsize=ara.font_size_normal)
        plt.tight_layout()
        plt.savefig(os.path.join(ara.dir,"total.png"),bbox_inches='tight')
        plt.clf()
        self._draw_result_sub(res=res)
        print(f"Done. Your results are in {ara.dir}")

    # prepare and show deep dive subgraphs for every single most important literal and all variables/literals that influence target class the most for important ones
    def _draw_result_sub(self,res=None,pre="",mult=1,init=True):
        """
        internal procedure for the draw result recursion
        """
        x = []
        y = []
        y_loc =[]
        colr = []
        colr_loc=[]
        x_grp = []
        y_grp = []
        colr_grp = []

        mult2=mult
        if mult2 < 1:
            mult2 = -1 / mult2

        px = 1 / plt.rcParams['figure.dpi']
        font = {'size': 8}

        for item in res:
            total_lift = mult*item['lift']
            mult3 = total_lift
            if mult3 < 1:
                mult3 = -1 / mult3
            lbl = item['vars'][0]['varname'] + "(" + str(item['vars'][0]['values_str']) + ")"
            val = total_lift
            val_loc = item['lift']
            col = 'g'
            col_loc = 'g'
            if val < 1:
                val = -1 / val
                col = 'r'
            if val_loc < 1:
                val_loc = -1 / val_loc
                col_loc='r'
            x.append(lbl)
            y.append(val)
            y_loc.append(val_loc)
            colr.append(col)
            colr_loc.append(col_loc)

            if len(item['sub'])>0:
                x_sub,y_sub,y_sub_loc,col_sub,col_sub_loc = self._draw_result_sub(res=item['sub'],pre=pre+" "+lbl,mult=total_lift,init=False)
                x_grp = x_grp + x_sub
                y_grp = y_grp + y_sub
                colr_grp = colr_grp + col_sub
                fig, axs = plt.subplots(2,figsize=(1920*px,1080*px))
                fig.suptitle('Local and global profiling of/with '+pre+" "+lbl,fontsize = ara.font_size_big)
                barlist2 = axs[1].barh(x_sub, y_sub)
                barlist3 = axs[0].barh(x_sub, y_sub_loc)
                for i in range(len(col_sub)):
                    barlist2[i].set_color(col_sub[i])
                    barlist3[i].set_color(col_sub_loc[i])
                if not(init):
                    x2 = range(5)
                    y2 = []
                    for ii in x2:
                        y2.append(mult)
                axs[1].set_title("GLOBAL LIFT VALUE WITH "+pre+" "+lbl+ " (baseline="+str("{:.1f}".format(mult3))+")",fontsize = ara.font_size_big)
                axs[0].set_title("LOCAL LIFT CHANGE FROM "+ pre+" "+lbl+ " (baseline="+str("{:.1f}".format(mult3))+")",fontsize = ara.font_size_big)
                #axs[1].yticks(fontsize=20)
                axs[0].tick_params(axis='y', labelsize=ara.font_size_normal)
                axs[1].tick_params(axis='y', labelsize=ara.font_size_normal)
                #axs[0].yticks(fontsize=20)
                fname = "".join(x if x.isalnum() else "_" for x in pre+" "+lbl)
                fname = os.path.join(ara.dir,fname+".png")
                fig.tight_layout()
                plt.savefig(fname,bbox_inches='tight')
                plt.clf()
        return x,y,y_loc,colr,colr_loc

    def clara(self,df:pandas.DataFrame=None,target=None,target_class=None,options=None, CL=None):
        """
        Categorical Lift-based Association Rules Analysis. Can be used for data / dependency profiling as well as XAI method for interpreting the model
        :param pandas.DataFrame df: pandas dataframe with input data
        :param string target: target variable of the dataset (profiling) or target prediction (for model explanation task)
        :param string target_class: target class of interest (when profiling more classes is needed, you can run this procedure in loop for all classes)
        :param dict options: dictionary with options. Valid options are max_depth (maximum depth of rules searched; default=2), min_base (minimum base of the rule searched, default 20), print_rules_on_the_fly (default 0)
        :param list CL: conditions for local explainability search (CL) - list of variables that can be used in a condition of association rule
        """
        if not(target in df.columns):
            print(f"Error: target variable ({target}) is not in dataframe.")
            exit(1)
        if not(target_class in df[target].unique()):
            print(f"Error: target class {target_class} is not present in ({target}) variable.")
            exit(1)
        if CL is None:
            print("List of variables for local search (parameter CL) need to be specified.")
            exit(1)

        succ = {'attributes': su, 'minlen': 1, 'maxlen': 1, 'type': 'con'}
        self.res = self._arar(df=df,target=target,target_class=target_class,options=options,cond_CL=CL)
