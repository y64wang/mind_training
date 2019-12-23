#!/bin/bash

#set -x

svn info $1 > /dev/null 2>&1
status=`echo $?` ; if [[ ${status} == 0 ]]; then echo "ECL link: $1 " ; else  echo "Error ECL link: $1" ; exit 1 ; fi

svn cat $1 > /tmp/ABIC_L1_ECL
status=`echo $?` ; if [[ ! ${status} == 0 ]]; then echo "Error ECL link: $1" ; exit 1 ; fi

source /tmp/ABIC_L1_ECL

ABIC_L1_CONFIG=".config"

if [[ ! -f $ABIC_L1_CONFIG ]]; then
    echo "$ABIC_L1_CONFIG file($ABIC_L1_CONFIG) not found!"
    exit 1
fi

if [[ ! -z $2 ]]; then
    echo "UL_PHY_LF tag: $2"
    ECL_UL_PHY_LF="/isource/svnroot/BTS_SC_UL_PHY/$2"
    svn info https://svne1.access.nsn.com/$ECL_UL_PHY_LF > /dev/null 2>&1
    status=`echo $?` ; if [[ ! ${status} == 0 ]]; then echo "Error UL_PHY_LF tag: $2" ; exit 1 ; fi
fi

if [[ ! -z $3 ]]; then
    echo "DL_PHY_LF tag: $3"
    ECL_DL_PHY_LF="/isource/svnroot/BTS_SC_PHY_TX/$3"
    svn info https://svne1.access.nsn.com/$ECL_DL_PHY_LF > /dev/null 2>&1
    status=`echo $?` ; if [[ ! ${status} == 0 ]]; then echo "Error DL_PHY_LF tag: $3" ; exit 1 ; fi
fi

if [[ ! -z $ECL_PS_REL ]]; then sed -i "s% PS_REL.*% PS_REL $ECL_PS_REL%"                                                $ABIC_L1_CONFIG; fi
if [[ ! -z $ECL_LFS_REL ]]; then sed -i "s% LFS_REL.*% LFS_REL $ECL_LFS_REL%"                                            $ABIC_L1_CONFIG; fi
if [[ ! -z $ECL_ISAR_GEN ]]; then sed -i "s% ISAR_GEN.*% ISAR_GEN $ECL_ISAR_GEN%"                                        $ABIC_L1_CONFIG; fi
if [[ ! -z $ECL_CASN ]]; then sed -i "s% CASN.*% CASN $ECL_CASN%"                                                        $ABIC_L1_CONFIG; fi
if [[ ! -z $ECL_UP_COMMON ]]; then sed -i "s% UP_COMMON.*% UP_COMMON $ECL_UP_COMMON%"                                    $ABIC_L1_CONFIG; fi
if [[ ! -z $ECL_TOOLSET ]]; then sed -i "s% TOOLSET.*% TOOLSET $ECL_TOOLSET%"                                            $ABIC_L1_CONFIG; fi
if [[ ! -z $ECL_SCM_CONFIG ]]; then sed -i "s% SCM_CONFIG.*% SCM_CONFIG $ECL_SCM_CONFIG%"                                $ABIC_L1_CONFIG; fi
if [[ ! -z $ECL_RTPMIF ]]; then sed -i "s% RTPMIF.*% RTPMIF $ECL_RTPMIF%"                                                $ABIC_L1_CONFIG; fi
if [[ ! -z $ECL_PM_COUNTERS_LTE ]]; then sed -i "s% PM_COUNTERS_LTE.*% PM_COUNTERS_LTE $ECL_PM_COUNTERS_LTE%"            $ABIC_L1_CONFIG; fi
if [[ ! -z $ECL_PM_COUNTERS_WCDMA ]]; then sed -i "s% PM_COUNTERS_WCDMA.*% PM_COUNTERS_WCDMA $ECL_PM_COUNTERS_WCDMA%"    $ABIC_L1_CONFIG; fi
if [[ ! -z $ECL_PM_COUNTERS_SBTS ]]; then sed -i "s% PM_COUNTERS_SBTS.*% PM_COUNTERS_SBTS $ECL_PM_COUNTERS_SBTS%"        $ABIC_L1_CONFIG; fi
if [[ ! -z $ECL_NSETAP ]]; then sed -i "s% NSETAP.*% NSETAP $ECL_NSETAP%"                                                $ABIC_L1_CONFIG; fi
if [[ ! -z $ECL_MSGIDLTE ]]; then sed -i "s% MSGIDLTE.*% MSGIDLTE $ECL_MSGIDLTE%"                                        $ABIC_L1_CONFIG; fi
if [[ ! -z $ECL_LTE_SCM ]]; then sed -i "s% LTE_SCM.*% LTE_SCM $ECL_LTE_SCM%"                                            $ABIC_L1_CONFIG; fi
if [[ ! -z $ECL_LOM ]]; then sed -i "s% LOM.*% LOM $ECL_LOM%"                                                            $ABIC_L1_CONFIG; fi
if [[ ! -z $ECL_LINSUP ]]; then sed -i "s% LINSUP.*% LINSUP $ECL_LINSUP%"                                                $ABIC_L1_CONFIG; fi
if [[ ! -z $ECL_LIM ]]; then sed -i "s% LIM.*% LIM $ECL_LIM%"                                                            $ABIC_L1_CONFIG; fi
if [[ ! -z $ECL_ISAR_XML ]]; then sed -i "s% ISAR_XML.*% ISAR_XML $ECL_ISAR_XML%"                                        $ABIC_L1_CONFIG; fi
if [[ ! -z $ECL_GLOBAL_ENV ]]; then sed -i "s% GLOBAL_ENV.*% GLOBAL_ENV $ECL_GLOBAL_ENV%"                                $ABIC_L1_CONFIG; fi
if [[ ! -z $ECL_ENV ]]; then sed -i "s% ENV.*% ENV $ECL_ENV%"                                                            $ABIC_L1_CONFIG; fi
if [[ ! -z $ECL_DSP_COMMON ]]; then sed -i "s% DSP_COMMON.*% DSP_COMMON $ECL_DSP_COMMON%"                                $ABIC_L1_CONFIG; fi
if [[ ! -z $ECL_COMMON_APPL_ENV ]]; then sed -i "s% COMMON_APPL_ENV.*% COMMON_APPL_ENV $ECL_COMMON_APPL_ENV%"            $ABIC_L1_CONFIG; fi
if [[ ! -z $ECL_CB_BB_SCRIPTS ]]; then sed -i "s% CB_BB_SCRIPTS.*% CB_BB_SCRIPTS $ECL_CB_BB_SCRIPTS%"                    $ABIC_L1_CONFIG; fi
if [[ ! -z $ECL_ARCH ]]; then sed -i "s% ARCH.*% ARCH $ECL_ARCH%"                                                        $ABIC_L1_CONFIG; fi
if [[ ! -z $ECL_LUNUM ]]; then sed -i "s% LUNUM.*% LUNUM $ECL_LUNUM%"                                                    $ABIC_L1_CONFIG; fi
if [[ ! -z $ECL_DL_PHY_LF ]]; then sed -i "s% DL_PHY_LF.*% DL_PHY_LF $ECL_DL_PHY_LF%"                                    $ABIC_L1_CONFIG; fi
if [[ ! -z $ECL_UL_PHY_LF ]]; then sed -i "s% UL_PHY_LF.*% UL_PHY_LF $ECL_UL_PHY_LF%"                                    $ABIC_L1_CONFIG; fi
if [[ ! -z $ECL_RTM ]]; then sed -i "s% RTM.*% RTM $ECL_RTM%"                                                            $ABIC_L1_CONFIG; fi

lteTools/production/bin/LTE update -l log
svn up .
