import streamlit as st
import re
import pandas as pd
import numpy as np

st.set_page_config(layout = "wide")



c = '''
15,64,1,14,1600,,5,4,RRCConnectionReconfiguration,241BBF8050918C400065082C0030041002C8820B000C014401900082C00300002019002002CEC09D2200290285970811F10A1B8C08808505CB8CEB9E290E31A48311460000200F95120390180018078380C805050EB9FF0CBDBF71B846039A8018010080080BF52ABE06A003280301A035B01FFB1C0B81FFB1C082EA207AEC5003A11BF400DDE6548E7F2A1D400600056341AA9A5BFFFFFFFFFFFFFFFF4318641480040506718240D0060B228485800008040188882FC0A9C0380194AC10E0040029AAE668000000001FFFFFFFE42243E41C1644165355CCD03FFFFFFFFFFFFFFFC844841A00E83A070C800354E573306FC844850410E9D036E19032EB8816088638ABF90241F09D03F4EF00031920A084281020F36C04195D3A771F1AD26AD8009A4D517000018830225994523FFFFFFFFFFF200083BE9B82210000002400D1141834009A0000620E044B3624F80205C6A1ECCCB497AC11B84370C6E20DC51B8C37D926F1AADD60108540740129C90B376E004048092616C401B842100058D2B2907064102002204012000111418020AC3211A801F8E92D73FAAA801F8E4402C6D0004004CD55521070E2048A163068E212044561C01102540710008814A038900440B501C5002206280E2C01103540718008810A058D004409502C700220528167C01103140B200187B0A0C8C3C02C2820580301D0FF346789999A47493400800C10ED608DC21B8637106E28DC61BC7FE851CE6293940A0802015C000200004000000000422B5515810C000421001F88E36480030101104007E238D92000C080421001F88E36488030301104007E238D92200C10CF6AA007E238D74808220060002040600800807019801F8E90000001002000402801101C001005E00083DC618618618618F0DFFC8BFFFC3CC660008000000570001E0004D5B01401080010284D0000204481301F00000003FA2525190000048A04944FC7629BA6C180
  
Release: 15, 
Version: 64, 
RB Id: 1, 
PCI: 014, 
EARFCN: 01600, 
Chan Type: 5, 
Msg Type: 4, 
Msg Name: RRCConnectionReconfiguration, 
Msg Body: 241BBF8050918C400065082C0030041002C8820B000C014401900082C00300002019002002CEC09D2200290285970811F10A1B8C08808505CB8CEB9E290E31A48311460000200F95120390180018078380C805050EB9FF0CBDBF71B846039A8018010080080BF52ABE06A003280301A035B01FFB1C0B81FFB1C082EA207AEC5003A11BF400DDE6548E7F2A1D400600056341AA9A5BFFFFFFFFFFFFFFFF4318641480040506718240D0060B228485800008040188882FC0A9C0380194AC10E0040029AAE668000000001FFFFFFFE42243E41C1644165355CCD03FFFFFFFFFFFFFFFC844841A00E83A070C800354E573306FC844850410E9D036E19032EB8816088638ABF90241F09D03F4EF00031920A084281020F36C04195D3A771F1AD26AD8009A4D517000018830225994523FFFFFFFFFFF200083BE9B82210000002400D1141834009A0000620E044B3624F80205C6A1ECCCB497AC11B84370C6E20DC51B8C37D926F1AADD60108540740129C90B376E004048092616C401B842100058D2B2907064102002204012000111418020AC3211A801F8E92D73FAAA801F8E4402C6D0004004CD55521070E2048A163068E212044561C01102540710008814A038900440B501C5002206280E2C01103540718008810A058D004409502C700220528167C01103140B200187B0A0C8C3C02C2820580301D0FF346789999A47493400800C10ED608DC21B8637106E28DC61BC7FE851CE6293940A0802015C000200004000000000422B5515810C000421001F88E36480030101104007E238D92000C080421001F88E36488030301104007E238D92200C10CF6AA007E238D74808220060002040600800807019801F8E90000001002000402801101C001005E00083DC618618618618F0DFFC8BFFFC3CC660008000000570001E0004D5B01401080010284D0000204481301F00000003FA2525190000048A04944FC7629BA6C180
LTE_Uu_RRC: DL_DCCH_Message
-   .   .message:- c1:- rrcConnectionReconfiguration
-   .   .   .   .   .rrc-TransactionIdentifier: 2
-   .   .   .   .   .criticalExtensions:- c1:- rrcConnectionReconfiguration-r8
-   .   .   .   .   .   .   .   .measConfig
-   .   .   .   .   .   .   .   .   .measObjectToRemoveList [ 0 ]: 9
-   .   .   .   .   .   .   .   .   .measObjectToRemoveList [ 1 ]: 10
-   .   .   .   .   .   .   .   .   .measObjectToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .measObjectId: 4
-   .   .   .   .   .   .   .   .   .   .measObject:- measObjectEUTRA
-   .   .   .   .   .   .   .   .   .   .   .   .carrierFreq: 101
-   .   .   .   .   .   .   .   .   .   .   .   .allowedMeasBandwidth: 0 ( mbw6)
-   .   .   .   .   .   .   .   .   .   .   .   .presenceAntennaPort1: 0 (False)
-   .   .   .   .   .   .   .   .   .   .   .   .neighCellConfig: 2
-   .   .   .   .   .   .   .   .   .   .   .   .measCycleSCell-r10: 0
-   .   .   .   .   .   .   .   .   .measObjectToAddModList [ 1 ]
-   .   .   .   .   .   .   .   .   .   .measObjectId: 5
-   .   .   .   .   .   .   .   .   .   .measObject:- measObjectEUTRA
-   .   .   .   .   .   .   .   .   .   .   .   .carrierFreq: 2850
-   .   .   .   .   .   .   .   .   .   .   .   .allowedMeasBandwidth: 0 ( mbw6)
-   .   .   .   .   .   .   .   .   .   .   .   .presenceAntennaPort1: 0 (False)
-   .   .   .   .   .   .   .   .   .   .   .   .neighCellConfig: 2
-   .   .   .   .   .   .   .   .   .   .   .   .measCycleSCell-r10: 0
-   .   .   .   .   .   .   .   .   .measObjectToAddModList [ 2 ]
-   .   .   .   .   .   .   .   .   .   .measObjectId: 6
-   .   .   .   .   .   .   .   .   .   .measObject:- measObjectEUTRA
-   .   .   .   .   .   .   .   .   .   .   .   .carrierFreq: 6400
-   .   .   .   .   .   .   .   .   .   .   .   .allowedMeasBandwidth: 0 ( mbw6)
-   .   .   .   .   .   .   .   .   .   .   .   .presenceAntennaPort1: 0 (False)
-   .   .   .   .   .   .   .   .   .   .   .   .neighCellConfig: 2
-   .   .   .   .   .   .   .   .   .   .   .   .measCycleSCell-r10: 0
-   .   .   .   .   .   .   .   .   .measObjectToAddModList [ 3 ]
-   .   .   .   .   .   .   .   .   .   .measObjectId: 1
-   .   .   .   .   .   .   .   .   .   .measObject:- measObjectEUTRA
-   .   .   .   .   .   .   .   .   .   .   .   .carrierFreq: 1600
-   .   .   .   .   .   .   .   .   .   .   .   .allowedMeasBandwidth: 0 ( mbw6)
-   .   .   .   .   .   .   .   .   .   .   .   .presenceAntennaPort1: 0 (False)
-   .   .   .   .   .   .   .   .   .   .   .   .neighCellConfig: 2
-   .   .   .   .   .   .   .   .   .   .   .   .cellsToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .cellIndex: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .physCellId: 359
-   .   .   .   .   .   .   .   .   .   .   .   .   .cellIndividualOffset: 12 ( dB_3)
-   .   .   .   .   .   .   .   .   .reportConfigToRemoveList [ 0 ]: 8
-   .   .   .   .   .   .   .   .   .reportConfigToRemoveList [ 1 ]: 10
-   .   .   .   .   .   .   .   .   .reportConfigToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 1
-   .   .   .   .   .   .   .   .   .   .reportConfig:- reportConfigEUTRA
-   .   .   .   .   .   .   .   .   .   .   .   .triggerType:- event
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .eventId:- eventA3
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .a3-Offset: 6 (3.0 dB)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .reportOnLeave: 0 (False)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .hysteresis: 2 (1.0 dB)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .timeToTrigger: 8 ( ms320)
-   .   .   .   .   .   .   .   .   .   .   .   .triggerQuantity: 0 ( rsrp)
-   .   .   .   .   .   .   .   .   .   .   .   .reportQuantity: 1 ( both)
-   .   .   .   .   .   .   .   .   .   .   .   .maxReportCells: 4
-   .   .   .   .   .   .   .   .   .   .   .   .reportInterval: 2 ( ms480)
-   .   .   .   .   .   .   .   .   .   .   .   .reportAmount: 7 ( infinity)
-   .   .   .   .   .   .   .   .   .reportConfigToAddModList [ 1 ]
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 2
-   .   .   .   .   .   .   .   .   .   .reportConfig:- reportConfigEUTRA
-   .   .   .   .   .   .   .   .   .   .   .   .triggerType:- event
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .eventId:- eventA2
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .a2-Threshold:- threshold-RSRP: 31 (-109.00 dBm)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .hysteresis: 2 (1.0 dB)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .timeToTrigger: 1 ( ms40)
-   .   .   .   .   .   .   .   .   .   .   .   .triggerQuantity: 0 ( rsrp)
-   .   .   .   .   .   .   .   .   .   .   .   .reportQuantity: 1 ( both)
-   .   .   .   .   .   .   .   .   .   .   .   .maxReportCells: 1
-   .   .   .   .   .   .   .   .   .   .   .   .reportInterval: 6 ( ms5120)
-   .   .   .   .   .   .   .   .   .   .   .   .reportAmount: 7 ( infinity)
-   .   .   .   .   .   .   .   .   .reportConfigToAddModList [ 2 ]
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 4
-   .   .   .   .   .   .   .   .   .   .reportConfig:- reportConfigEUTRA
-   .   .   .   .   .   .   .   .   .   .   .   .triggerType:- event
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .eventId:- eventA2
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .a2-Threshold:- threshold-RSRP: 16 (-124.00 dBm)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .hysteresis: 2 (1.0 dB)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .timeToTrigger: 1 ( ms40)
-   .   .   .   .   .   .   .   .   .   .   .   .triggerQuantity: 0 ( rsrp)
-   .   .   .   .   .   .   .   .   .   .   .   .reportQuantity: 1 ( both)
-   .   .   .   .   .   .   .   .   .   .   .   .maxReportCells: 1
-   .   .   .   .   .   .   .   .   .   .   .   .reportInterval: 2 ( ms480)
-   .   .   .   .   .   .   .   .   .   .   .   .reportAmount: 7 ( infinity)
-   .   .   .   .   .   .   .   .   .measIdToRemoveList [ 0 ]: 25
-   .   .   .   .   .   .   .   .   .measIdToRemoveList [ 1 ]: 26
-   .   .   .   .   .   .   .   .   .measIdToRemoveList [ 2 ]: 27
-   .   .   .   .   .   .   .   .   .measIdToRemoveList [ 3 ]: 29
-   .   .   .   .   .   .   .   .   .measIdToRemoveList [ 4 ]: 31
-   .   .   .   .   .   .   .   .   .measIdToRemoveList [ 5 ]: 6
-   .   .   .   .   .   .   .   .   .measIdToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .measId: 8
-   .   .   .   .   .   .   .   .   .   .measObjectId: 4
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 4
-   .   .   .   .   .   .   .   .   .measIdToAddModList [ 1 ]
-   .   .   .   .   .   .   .   .   .   .measId: 10
-   .   .   .   .   .   .   .   .   .   .measObjectId: 5
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 4
-   .   .   .   .   .   .   .   .   .measIdToAddModList [ 2 ]
-   .   .   .   .   .   .   .   .   .   .measId: 3
-   .   .   .   .   .   .   .   .   .   .measObjectId: 6
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 4
-   .   .   .   .   .   .   .   .   .measIdToAddModList [ 3 ]
-   .   .   .   .   .   .   .   .   .   .measId: 1
-   .   .   .   .   .   .   .   .   .   .measObjectId: 1
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 1
-   .   .   .   .   .   .   .   .   .measIdToAddModList [ 4 ]
-   .   .   .   .   .   .   .   .   .   .measId: 2
-   .   .   .   .   .   .   .   .   .   .measObjectId: 1
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 2
-   .   .   .   .   .   .   .   .   .quantityConfig
-   .   .   .   .   .   .   .   .   .   .quantityConfigEUTRA
-   .   .   .   .   .   .   .   .   .   .   .filterCoefficientRSRQ: 10 ( fc11)
-   .   .   .   .   .   .   .   .   .   .quantityConfigUTRA
-   .   .   .   .   .   .   .   .   .   .   .measQuantityUTRA-FDD: 0 ( cpich_RSCP)
-   .   .   .   .   .   .   .   .   .   .   .measQuantityUTRA-TDD: 0 ( pccpch_RSCP)
-   .   .   .   .   .   .   .   .   .   .quantityConfigGERAN
-   .   .   .   .   .   .   .   .   .   .   .measQuantityGERAN: 0 ( rssi)
-   .   .   .   .   .   .   .   .   .   .   .filterCoefficient: 4 ( fc4)
-   .   .   .   .   .   .   .   .   .   .quantityConfigUTRA-v1020
-   .   .   .   .   .   .   .   .   .   .quantityConfigNRList-r15 [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .measQuantityCellNR-r15
-   .   .   .   .   .   .   .   .mobilityControlInfo
-   .   .   .   .   .   .   .   .   .targetPhysCellId: 14
-   .   .   .   .   .   .   .   .   .carrierFreq
-   .   .   .   .   .   .   .   .   .   .dl-CarrierFreq: 1600
-   .   .   .   .   .   .   .   .   .carrierBandwidth
-   .   .   .   .   .   .   .   .   .   .dl-Bandwidth: 5 ( n100)
-   .   .   .   .   .   .   .   .   .additionalSpectrumEmission: 1
-   .   .   .   .   .   .   .   .   .t304: 5 ( ms1000)
-   .   .   .   .   .   .   .   .   .newUE-Identity: 3769 (0xEB9)
-   .   .   .   .   .   .   .   .   .radioResourceConfigCommon
-   .   .   .   .   .   .   .   .   .   .rach-ConfigCommon
-   .   .   .   .   .   .   .   .   .   .   .preambleInfo
-   .   .   .   .   .   .   .   .   .   .   .   .numberOfRA-Preambles: 12 ( n52)
-   .   .   .   .   .   .   .   .   .   .   .powerRampingParameters
-   .   .   .   .   .   .   .   .   .   .   .   .powerRampingStep: 2 ( dB4)
-   .   .   .   .   .   .   .   .   .   .   .   .preambleInitialReceivedTargetPower: 15 ( dBm_90)
-   .   .   .   .   .   .   .   .   .   .   .ra-SupervisionInfo
-   .   .   .   .   .   .   .   .   .   .   .   .preambleTransMax: 6 ( n10)
-   .   .   .   .   .   .   .   .   .   .   .   .ra-ResponseWindowSize: 7 ( sf10)
-   .   .   .   .   .   .   .   .   .   .   .   .mac-ContentionResolutionTimer: 7 ( sf64)
-   .   .   .   .   .   .   .   .   .   .   .maxHARQ-Msg3Tx: 4
-   .   .   .   .   .   .   .   .   .   .prach-Config
-   .   .   .   .   .   .   .   .   .   .   .rootSequenceIndex: 110
-   .   .   .   .   .   .   .   .   .   .   .prach-ConfigInfo
-   .   .   .   .   .   .   .   .   .   .   .   .prach-ConfigIndex: 4
-   .   .   .   .   .   .   .   .   .   .   .   .highSpeedFlag: 0 (False)
-   .   .   .   .   .   .   .   .   .   .   .   .zeroCorrelationZoneConfig: 12 (12)
-   .   .   .   .   .   .   .   .   .   .   .   .prach-FreqOffset: 3
-   .   .   .   .   .   .   .   .   .   .pdsch-ConfigCommon
-   .   .   .   .   .   .   .   .   .   .   .referenceSignalPower: 17 (17.0 dBm)
-   .   .   .   .   .   .   .   .   .   .   .p-b: 1
-   .   .   .   .   .   .   .   .   .   .pusch-ConfigCommon
-   .   .   .   .   .   .   .   .   .   .   .pusch-ConfigBasic
-   .   .   .   .   .   .   .   .   .   .   .   .n-SB: 1 (1)
-   .   .   .   .   .   .   .   .   .   .   .   .hoppingMode: 0 ( interSubFrame)
-   .   .   .   .   .   .   .   .   .   .   .   .pusch-HoppingOffset: 0
-   .   .   .   .   .   .   .   .   .   .   .   .enable64QAM: 1 (True)
-   .   .   .   .   .   .   .   .   .   .   .ul-ReferenceSignalsPUSCH
-   .   .   .   .   .   .   .   .   .   .   .   .groupHoppingEnabled: 1 (True)
-   .   .   .   .   .   .   .   .   .   .   .   .groupAssignmentPUSCH: 0
-   .   .   .   .   .   .   .   .   .   .   .   .sequenceHoppingEnabled: 0 (0)
-   .   .   .   .   .   .   .   .   .   .   .   .cyclicShift: 0
-   .   .   .   .   .   .   .   .   .   .phich-Config
-   .   .   .   .   .   .   .   .   .   .   .phich-Duration: 0 ( normal)
-   .   .   .   .   .   .   .   .   .   .   .phich-Resource: 2 ( one)
-   .   .   .   .   .   .   .   .   .   .pucch-ConfigCommon
-   .   .   .   .   .   .   .   .   .   .   .deltaPUCCH-Shift: 0 ( ds1)
-   .   .   .   .   .   .   .   .   .   .   .nRB-CQI: 2
-   .   .   .   .   .   .   .   .   .   .   .nCS-AN: 0
-   .   .   .   .   .   .   .   .   .   .   .n1PUCCH-AN: 8
-   .   .   .   .   .   .   .   .   .   .soundingRS-UL-ConfigCommon:- release: null
-   .   .   .   .   .   .   .   .   .   .uplinkPowerControlCommon
-   .   .   .   .   .   .   .   .   .   .   .p0-NominalPUSCH: -103 (-103.0 dBm)
-   .   .   .   .   .   .   .   .   .   .   .alpha: 7 ( al1)
-   .   .   .   .   .   .   .   .   .   .   .p0-NominalPUCCH: -117 (-117.0 dBm)
-   .   .   .   .   .   .   .   .   .   .   .deltaFList-PUCCH
-   .   .   .   .   .   .   .   .   .   .   .   .deltaF-PUCCH-Format1: 1 ( deltaF0)
-   .   .   .   .   .   .   .   .   .   .   .   .deltaF-PUCCH-Format1b: 1 ( deltaF3)
-   .   .   .   .   .   .   .   .   .   .   .   .deltaF-PUCCH-Format2: 1 ( deltaF0)
-   .   .   .   .   .   .   .   .   .   .   .   .deltaF-PUCCH-Format2a: 1 ( deltaF0)
-   .   .   .   .   .   .   .   .   .   .   .   .deltaF-PUCCH-Format2b: 1 ( deltaF0)
-   .   .   .   .   .   .   .   .   .   .   .deltaPreambleMsg3: 6 (12.0 dB)
-   .   .   .   .   .   .   .   .   .   .antennaInfoCommon
-   .   .   .   .   .   .   .   .   .   .   .antennaPortsCount: 2 ( an4)
-   .   .   .   .   .   .   .   .   .   .ul-CyclicPrefixLength: 0 ( len1)
-   .   .   .   .   .   .   .   .   .   .uplinkPowerControlCommon-v1020
-   .   .   .   .   .   .   .   .   .   .   .deltaF-PUCCH-Format3-r10: 1
-   .   .   .   .   .   .   .   .   .   .   .deltaF-PUCCH-Format1bCS-r10: 1
-   .   .   .   .   .   .   .   .   .   .pusch-ConfigCommon-v1270
-   .   .   .   .   .   .   .   .   .   .   .enable64QAM-v1270: 0
-   .   .   .   .   .   .   .   .   .rach-ConfigDedicated
-   .   .   .   .   .   .   .   .   .   .ra-PreambleIndex: 52
-   .   .   .   .   .   .   .   .   .   .ra-PRACH-MaskIndex: 0
-   .   .   .   .   .   .   .   .radioResourceConfigDedicated
-   .   .   .   .   .   .   .   .   .srb-ToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .srb-Identity: 1
-   .   .   .   .   .   .   .   .   .   .rlc-Config:- explicitValue:- am
-   .   .   .   .   .   .   .   .   .   .   .   .   .ul-AM-RLC
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .t-PollRetransmit: 15 ( ms80)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .pollPDU: 7 ( pInfinity)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .pollByte: 14 ( kBinfinity)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .maxRetxThreshold: 6 ( t16)
-   .   .   .   .   .   .   .   .   .   .   .   .   .dl-AM-RLC
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .t-Reordering: 7 ( ms35)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .t-StatusProhibit: 0 ( ms0)
-   .   .   .   .   .   .   .   .   .   .logicalChannelConfig:- defaultValue: null
-   .   .   .   .   .   .   .   .   .srb-ToAddModList [ 1 ]
-   .   .   .   .   .   .   .   .   .   .srb-Identity: 2
-   .   .   .   .   .   .   .   .   .   .rlc-Config:- explicitValue:- am
-   .   .   .   .   .   .   .   .   .   .   .   .   .ul-AM-RLC
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .t-PollRetransmit: 15 ( ms80)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .pollPDU: 7 ( pInfinity)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .pollByte: 14 ( kBinfinity)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .maxRetxThreshold: 6 ( t16)
-   .   .   .   .   .   .   .   .   .   .   .   .   .dl-AM-RLC
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .t-Reordering: 7 ( ms35)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .t-StatusProhibit: 0 ( ms0)
-   .   .   .   .   .   .   .   .   .   .logicalChannelConfig:- defaultValue: null
-   .   .   .   .   .   .   .   .   .drb-ToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .eps-BearerIdentity: 5
-   .   .   .   .   .   .   .   .   .   .drb-Identity: 3
-   .   .   .   .   .   .   .   .   .   .rlc-Config:- am
-   .   .   .   .   .   .   .   .   .   .   .   .ul-AM-RLC
-   .   .   .   .   .   .   .   .   .   .   .   .   .t-PollRetransmit: 15 ( ms80)
-   .   .   .   .   .   .   .   .   .   .   .   .   .pollPDU: 2 ( p16)
-   .   .   .   .   .   .   .   .   .   .   .   .   .pollByte: 14 ( kBinfinity)
-   .   .   .   .   .   .   .   .   .   .   .   .   .maxRetxThreshold: 6 ( t16)
-   .   .   .   .   .   .   .   .   .   .   .   .dl-AM-RLC
-   .   .   .   .   .   .   .   .   .   .   .   .   .t-Reordering: 5 ( ms25)
-   .   .   .   .   .   .   .   .   .   .   .   .   .t-StatusProhibit: 0 ( ms0)
-   .   .   .   .   .   .   .   .   .   .logicalChannelIdentity: 3
-   .   .   .   .   .   .   .   .   .   .logicalChannelConfig
-   .   .   .   .   .   .   .   .   .   .   .ul-SpecificParameters
-   .   .   .   .   .   .   .   .   .   .   .   .priority: 11
-   .   .   .   .   .   .   .   .   .   .   .   .prioritisedBitRate: 1
-   .   .   .   .   .   .   .   .   .   .   .   .bucketSizeDuration: 0
-   .   .   .   .   .   .   .   .   .   .   .   .logicalChannelGroup: 3
-   .   .   .   .   .   .   .   .   .mac-MainConfig:- explicitValue
-   .   .   .   .   .   .   .   .   .   .   .ul-SCH-Config
-   .   .   .   .   .   .   .   .   .   .   .   .maxHARQ-Tx: 4 ( n5)
-   .   .   .   .   .   .   .   .   .   .   .   .periodicBSR-Timer: 0 ( sf5)
-   .   .   .   .   .   .   .   .   .   .   .   .retxBSR-Timer: 0 ( sf320)
-   .   .   .   .   .   .   .   .   .   .   .   .ttiBundling: 0 (False)
-   .   .   .   .   .   .   .   .   .   .   .drx-Config:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .onDurationTimer: 7 ( psf10)
-   .   .   .   .   .   .   .   .   .   .   .   .   .drx-InactivityTimer: 15 ( psf200)
-   .   .   .   .   .   .   .   .   .   .   .   .   .drx-RetransmissionTimer: 1 ( psf2)
-   .   .   .   .   .   .   .   .   .   .   .   .   .longDRX-CycleStartOffset:- sf320: 164
-   .   .   .   .   .   .   .   .   .   .   .   .   .shortDRX
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .shortDRX-Cycle: 7 ( sf40)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .drxShortCycleTimer: 4
-   .   .   .   .   .   .   .   .   .   .   .timeAlignmentTimerDedicated: 7 ( infinity)
-   .   .   .   .   .   .   .   .   .   .   .phr-Config:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .periodicPHR-Timer: 4 ( sf200)
-   .   .   .   .   .   .   .   .   .   .   .   .   .prohibitPHR-Timer: 5 ( sf200)
-   .   .   .   .   .   .   .   .   .   .   .   .   .dl-PathlossChange: 1 ( dB3)
-   .   .   .   .   .   .   .   .   .   .   .mac-MainConfig-v1020
-   .   .   .   .   .   .   .   .   .   .   .dualConnectivityPHR:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .phr-ModeOtherCG-r12: 1
-   .   .   .   .   .   .   .   .   .physicalConfigDedicated
-   .   .   .   .   .   .   .   .   .   .pdsch-ConfigDedicated
-   .   .   .   .   .   .   .   .   .   .   .p-a: 2 ( dB_3)
-   .   .   .   .   .   .   .   .   .   .pusch-ConfigDedicated
-   .   .   .   .   .   .   .   .   .   .   .betaOffset-ACK-Index: 10
-   .   .   .   .   .   .   .   .   .   .   .betaOffset-RI-Index: 9
-   .   .   .   .   .   .   .   .   .   .   .betaOffset-CQI-Index: 10
-   .   .   .   .   .   .   .   .   .   .antennaInfo:- explicitValue
-   .   .   .   .   .   .   .   .   .   .   .   .transmissionMode: 3 ( tm4)
-   .   .   .   .   .   .   .   .   .   .   .   .codebookSubsetRestriction:- n4TxAntenna-tm4: 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 
-   .   .   .   .   .   .   .   .   .   .   .   .ue-TransmitAntennaSelection:- release: null
-   .   .   .   .   .   .   .   .   .   .schedulingRequestConfig:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .sr-PUCCH-ResourceIndex: 99
-   .   .   .   .   .   .   .   .   .   .   .   .sr-ConfigIndex: 12
-   .   .   .   .   .   .   .   .   .   .   .   .dsr-TransMax: 4 ( n64)
-   .   .   .   .   .   .   .   .   .   .cqi-ReportConfig-r10
-   .   .   .   .   .   .   .   .   .   .   .cqi-ReportAperiodic-r10:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .cqi-ReportModeAperiodic-r10: 4 ( rm31)
-   .   .   .   .   .   .   .   .   .   .   .   .   .aperiodicCSI-Trigger-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .trigger1-r10: 96
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .trigger2-r10: 144
-   .   .   .   .   .   .   .   .   .   .   .nomPDSCH-RS-EPRE-Offset: 0
-   .   .   .   .   .   .   .   .   .   .   .cqi-ReportPeriodic-r10:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .cqi-PUCCH-ResourceIndex-r10: 12
-   .   .   .   .   .   .   .   .   .   .   .   .   .cqi-pmi-ConfigIndex: 89
-   .   .   .   .   .   .   .   .   .   .   .   .   .cqi-FormatIndicatorPeriodic-r10:- widebandCQI-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .ri-ConfigIndex: 322
-   .   .   .   .   .   .   .   .   .   .   .   .   .simultaneousAckNackAndCQI: 0
-   .   .   .   .   .   .   .   .   .   .pucch-ConfigDedicated-v1020
-   .   .   .   .   .   .   .   .   .   .   .pucch-Format-r10:- format3-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .n3PUCCH-AN-List-r13 [ 0 ]: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .n3PUCCH-AN-List-r13 [ 1 ]: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .n3PUCCH-AN-List-r13 [ 2 ]: 2
-   .   .   .   .   .   .   .   .   .   .   .   .   .n3PUCCH-AN-List-r13 [ 3 ]: 3
-   .   .   .   .   .   .   .   .securityConfigHO
-   .   .   .   .   .   .   .   .   .handoverType:- intraLTE
-   .   .   .   .   .   .   .   .   .   .   .securityAlgorithmConfig
-   .   .   .   .   .   .   .   .   .   .   .   .cipheringAlgorithm: 1 ( eea1)
-   .   .   .   .   .   .   .   .   .   .   .   .integrityProtAlgorithm: 1 ( eia1)
-   .   .   .   .   .   .   .   .   .   .   .keyChangeIndicator: 0 (False)
-   .   .   .   .   .   .   .   .   .   .   .nextHopChainingCount: 0
-   .   .   .   .   .   .   .   .nonCriticalExtension
-   .   .   .   .   .   .   .   .   .nonCriticalExtension
-   .   .   .   .   .   .   .   .   .   .fullConfig-r9: 0 ( true)
-   .   .   .   .   .   .   .   .   .   .nonCriticalExtension
-   .   .   .   .   .   .   .   .   .   .   .sCellToReleaseList-r10 [ 0 ]: 1
-   .   .   .   .   .   .   .   .   .   .   .sCellToReleaseList-r10 [ 1 ]: 2
-   .   .   .   .   .   .   .   .   .   .   .sCellToReleaseList-r10 [ 2 ]: 3
-   .   .   .   .   .   .   .   .   .   .   .sCellToAddModList-r10 [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .sCellIndex-r10: 1
-   .   .   .   .   .   .   .   .   .   .   .   .cellIdentification-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .physCellId-r10: 14
-   .   .   .   .   .   .   .   .   .   .   .   .   .dl-CarrierFreq-r10: 101
-   .   .   .   .   .   .   .   .   .   .   .   .radioResourceConfigCommonSCell-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .nonUL-Configuration-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .dl-Bandwidth-r10: 5
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .antennaInfoCommon-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .antennaPortsCount: 2 ( an4)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .mbsfn-SubframeConfigList-r10 [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .radioframeAllocationPeriod: 2 ( n4)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .radioframeAllocationOffset: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .subframeAllocation:- fourFrames: 12584960
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .phich-Config-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .phich-Duration: 0 ( normal)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .phich-Resource: 2 ( one)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .pdsch-ConfigCommon-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .referenceSignalPower: 17 (17.0 dBm)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .p-b: 1
-   .   .   .   .   .   .   .   .   .   .   .   .radioResourceConfigDedicatedSCell-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .physicalConfigDedicatedSCell-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .nonUL-Configuration-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .antennaInfo-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .transmissionMode-r10: 3 ( tm4)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .codebookSubsetRestriction-r10: 0000 0000 0000 0000 0000 0000 0000 0000 1111 1111 1111 1111 1111 1111 1111 1111 
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .ue-TransmitAntennaSelection:- release: null
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pdsch-ConfigDedicated-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .p-a: 2 ( dB_3)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .ul-Configuration-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .cqi-ReportConfigSCell-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .cqi-ReportModeAperiodic-r10: 4 ( rm31)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nomPDSCH-RS-EPRE-Offset-r10: 0
-   .   .   .   .   .   .   .   .   .   .   .sCellToAddModList-r10 [ 1 ]
-   .   .   .   .   .   .   .   .   .   .   .   .sCellIndex-r10: 2
-   .   .   .   .   .   .   .   .   .   .   .   .cellIdentification-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .physCellId-r10: 14
-   .   .   .   .   .   .   .   .   .   .   .   .   .dl-CarrierFreq-r10: 2850
-   .   .   .   .   .   .   .   .   .   .   .   .radioResourceConfigCommonSCell-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .nonUL-Configuration-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .dl-Bandwidth-r10: 5
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .antennaInfoCommon-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .antennaPortsCount: 2 ( an4)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .phich-Config-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .phich-Duration: 0 ( normal)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .phich-Resource: 2 ( one)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .pdsch-ConfigCommon-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .referenceSignalPower: 17 (17.0 dBm)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .p-b: 1
-   .   .   .   .   .   .   .   .   .   .   .   .radioResourceConfigDedicatedSCell-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .physicalConfigDedicatedSCell-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .nonUL-Configuration-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .antennaInfo-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .transmissionMode-r10: 3 ( tm4)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .codebookSubsetRestriction-r10: 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .ue-TransmitAntennaSelection:- release: null
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pdsch-ConfigDedicated-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .p-a: 2 ( dB_3)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .ul-Configuration-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .cqi-ReportConfigSCell-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .cqi-ReportModeAperiodic-r10: 4 ( rm31)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nomPDSCH-RS-EPRE-Offset-r10: 0
-   .   .   .   .   .   .   .   .   .   .   .   .antennaInfoDedicatedSCell-v10i0
-   .   .   .   .   .   .   .   .   .   .   .   .   .maxLayersMIMO-r10: 1
-   .   .   .   .   .   .   .   .   .   .   .sCellToAddModList-r10 [ 2 ]
-   .   .   .   .   .   .   .   .   .   .   .   .sCellIndex-r10: 3
-   .   .   .   .   .   .   .   .   .   .   .   .cellIdentification-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .physCellId-r10: 14
-   .   .   .   .   .   .   .   .   .   .   .   .   .dl-CarrierFreq-r10: 6400
-   .   .   .   .   .   .   .   .   .   .   .   .radioResourceConfigCommonSCell-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .nonUL-Configuration-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .dl-Bandwidth-r10: 3
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .antennaInfoCommon-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .antennaPortsCount: 1 ( an2)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .phich-Config-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .phich-Duration: 0 ( normal)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .phich-Resource: 2 ( one)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .pdsch-ConfigCommon-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .referenceSignalPower: 18 (18.0 dBm)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .p-b: 1
-   .   .   .   .   .   .   .   .   .   .   .   .radioResourceConfigDedicatedSCell-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .physicalConfigDedicatedSCell-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .nonUL-Configuration-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .antennaInfo-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .transmissionMode-r10: 3 ( tm4)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .codebookSubsetRestriction-r10: 63
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .ue-TransmitAntennaSelection:- release: null
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pdsch-ConfigDedicated-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .p-a: 2 ( dB_3)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .ul-Configuration-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .cqi-ReportConfigSCell-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .cqi-ReportModeAperiodic-r10: 4 ( rm31)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nomPDSCH-RS-EPRE-Offset-r10: 0
-   .   .   .   .   .   .   .   .   .   .   .nonCriticalExtension
-   .   .   .   .   .   .   .   .   .   .   .   .nonCriticalExtension
-   .   .   .   .   .   .   .   .   .   .   .   .   .nonCriticalExtension
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .nonCriticalExtension
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nonCriticalExtension
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nr-Config-r15:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .endc-ReleaseAndAdd-r15: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nr-SecondaryCellGroupConfig-r15: 0x0c81975c40b04431c55fc8120f84e81fa7780018c90504214081079b6020cae9d3b8f8d69356c004d26a8b80000c418112cca291fffffffffff900041df4dc1108000001200688a0c1a
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .---EMBEDDED CONTAINER DECODING START---
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .NR_Uu_RRC: 
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .RRCReconfiguration
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .rrc-TransactionIdentifier: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .criticalExtensions:- rrcReconfiguration
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .secondaryCellGroup
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .cellGroupId: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .rlc-BearerToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .logicalChannelIdentity: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .servedRadioBearer:- drb-Identity: 3
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .rlc-Config:- am
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .ul-AM-RLC
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .sn-FieldLength: 1 ( size18)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .t-PollRetransmit: 7 ( ms40)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pollPDU: 2 ( p16)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pollByte: 43 ( infinity)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .maxRetxThreshold: 7 ( t32)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .dl-AM-RLC
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .sn-FieldLength: 1 ( size18)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .t-Reassembly: 4 ( ms20)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .t-StatusProhibit: 2 ( ms10)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .mac-LogicalChannelConfig
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .ul-SpecificParameters
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .priority: 15
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .prioritisedBitRate: 1 ( kBps8)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .bucketSizeDuration: 3 ( ms50)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .logicalChannelGroup: 5
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .schedulingRequestID: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .logicalChannelSR-Mask: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .logicalChannelSR-DelayTimerApplied: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .mac-CellGroupConfig
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .drx-Config:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .drx-onDurationTimer:- milliSeconds: 7 ( ms10)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .drx-InactivityTimer: 15 ( ms100)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .drx-HARQ-RTT-TimerDL: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .drx-HARQ-RTT-TimerUL: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .drx-RetransmissionTimerDL: 6 ( sl16)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .drx-RetransmissionTimerUL: 6 ( sl16)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .drx-LongCycleStartOffset:- ms160: 5
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .drx-SlotOffset: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .schedulingRequestConfig
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .schedulingRequestToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .schedulingRequestId: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .sr-ProhibitTimer: 2 ( ms4)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .sr-TransMax: 4 ( n64)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .bsr-Config
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .periodicBSR-Timer: 2 ( sf10)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .retxBSR-Timer: 0 ( sf10)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .tag-Config
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .tag-ToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .tag-Id: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .timeAlignmentTimer: 7 ( infinity)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .phr-Config:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .phr-PeriodicTimer: 3 ( sf100)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .phr-ProhibitTimer: 3 ( sf50)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .phr-Tx-PowerFactorChange: 1 ( dB3)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .multiplePHR: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .dummy: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .phr-Type2OtherCell: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .phr-ModeOtherCG: 0 ( real)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .skipUplinkTxDynamic: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .physicalCellGroupConfig
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .p-NR-FR1: 20
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pdsch-HARQ-ACK-Codebook: 1 ( dynamic)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .spCellConfig
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .servCellIndex: 7
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .reconfigurationWithSync
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .spCellConfigCommon
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .physCellId: 909 (909)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .downlinkConfigCommon
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .frequencyInfoDL
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .absoluteFrequencySSB: 633696
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .frequencyBandList [ 0 ]: 78
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .absoluteFrequencyPointA: 633390
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .scs-SpecificCarrierList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .offsetToCarrier: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .subcarrierSpacing: 1 ( kHz30)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .carrierBandwidth: 273
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .initialDownlinkBWP
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .genericParameters
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .locationAndBandwidth: 1099
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .subcarrierSpacing: 1 ( kHz30)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pdcch-ConfigCommon:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .commonControlResourceSet
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .controlResourceSetId: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .frequencyDomainResources: 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .duration: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .cce-REG-MappingType:- nonInterleaved: null
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .precoderGranularity: 0 ( sameAsREG_bundle)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .tci-StatesPDCCH-ToAddList [ 0 ]: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pdcch-DMRS-ScramblingID: 1917
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .commonSearchSpaceList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .searchSpaceId: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .controlResourceSetId: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .monitoringSlotPeriodicityAndOffset:- sl1: null
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .monitoringSymbolsWithinSlot: 8192
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofCandidates
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .aggregationLevel1: 0 ( n0)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .aggregationLevel2: 0 ( n0)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .aggregationLevel4: 0 ( n0)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .aggregationLevel8: 0 ( n0)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .aggregationLevel16: 2 ( n2)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .searchSpaceType:- commonX
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .dci-Format0-0-AndFormat1-0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .ra-SearchSpace: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pdsch-ConfigCommon:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pdsch-TimeDomainAllocationList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .mappingType: 0 ( typeA)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startSymbolAndLength: 40
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pdsch-TimeDomainAllocationList [ 1 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .mappingType: 0 ( typeA)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startSymbolAndLength: 96
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .uplinkConfigCommon
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .frequencyInfoUL
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .frequencyBandList [ 0 ]: 78
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .scs-SpecificCarrierList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .offsetToCarrier: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .subcarrierSpacing: 1 ( kHz30)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .carrierBandwidth: 273
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .initialUplinkBWP
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .genericParameters
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .locationAndBandwidth: 1099
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .subcarrierSpacing: 1 ( kHz30)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .rach-ConfigCommon:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .rach-ConfigGeneric
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .prach-ConfigurationIndex: 159
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .msg1-FDM: 0 ( one)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .msg1-FrequencyStart: 2
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .zeroCorrelationZoneConfig: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .preambleReceivedTargetPower: -110
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .preambleTransMax: 6 ( n10)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .powerRampingStep: 2 ( dB4)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .ra-ResponseWindow: 4 ( sl10)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .totalNumberOfRA-Preambles: 16
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .ssb-perRACH-OccasionAndCB-PreamblesPerSSB:- one: 3 ( n16)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .ra-ContentionResolutionTimer: 1 ( sf16)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .prach-RootSequenceIndex:- l139: 45
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .msg1-SubcarrierSpacing: 1 ( kHz30)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .restrictedSetConfig: 0 ( unrestrictedSet)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pusch-ConfigCommon:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .groupHoppingEnabledTransformPrecoding: 0 ( enabled)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pusch-TimeDomainAllocationList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .k2: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .mappingType: 0 ( typeA)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startSymbolAndLength: 27
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pusch-TimeDomainAllocationList [ 1 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .k2: 2
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .mappingType: 0 ( typeA)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startSymbolAndLength: 27
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pusch-TimeDomainAllocationList [ 2 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .k2: 3
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .mappingType: 0 ( typeA)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startSymbolAndLength: 27
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pusch-TimeDomainAllocationList [ 3 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .k2: 4
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .mappingType: 0 ( typeA)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startSymbolAndLength: 27
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pusch-TimeDomainAllocationList [ 4 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .k2: 5
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .mappingType: 0 ( typeA)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startSymbolAndLength: 27
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pusch-TimeDomainAllocationList [ 5 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .k2: 6
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .mappingType: 0 ( typeA)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startSymbolAndLength: 27
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .msg3-DeltaPreamble: 6
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .p0-NominalWithGrant: -102
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pucch-ConfigCommon:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pucch-GroupHopping: 1 ( enable)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .hoppingId: 909
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .p0-nominal: -116
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .dummy: 7 ( infinity)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .n-TimingAdvanceOffset: 1 ( n25600)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .ssb-PositionsInBurst:- mediumBitmap: 128
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .ssb-periodicityServingCell: 2 ( ms20)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .dmrs-TypeA-Position: 0 ( pos2)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .ssbSubcarrierSpacing: 1 ( kHz30)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .tdd-UL-DL-ConfigurationCommon
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .referenceSubcarrierSpacing: 1 ( kHz30)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pattern1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .dl-UL-TransmissionPeriodicity: 5 ( ms2p5)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofDownlinkSlots: 3
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofDownlinkSymbols: 10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofUplinkSlots: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofUplinkSymbols: 2
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .ss-PBCH-BlockPower: 18
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .newUE-Identity: 18521
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .t304: 5 ( ms1000)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .rlf-TimersAndConstants:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .t310: 6 ( ms2000)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .n310: 7 ( n20)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .n311: 0 ( n1)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .t311: 1 ( ms3000)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .spCellConfigDedicated
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .initialDownlinkBWP
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pdcch-Config:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .searchSpacesToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .searchSpaceId: 2
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .controlResourceSetId: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .monitoringSlotPeriodicityAndOffset:- sl1: null
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .monitoringSymbolsWithinSlot: 8192
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofCandidates
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .aggregationLevel1: 5 ( n5)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .aggregationLevel2: 4 ( n4)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .aggregationLevel4: 3 ( n3)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .aggregationLevel8: 2 ( n2)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .aggregationLevel16: 2 ( n2)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .searchSpaceType:- ue-Specific
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .dci-Formats: 1 ( formats0_1_And_1_1)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pdsch-Config:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .dmrs-DownlinkForPDSCH-MappingTypeA:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .dmrs-AdditionalPosition: 1 ( pos1)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .tci-StatesToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .tci-StateId: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .qcl-Type1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .bwp-Id: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .referenceSignal:- ssb: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .qcl-Type: 2 ( typeC)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .tci-StatesToAddModList [ 1 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .tci-StateId: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .qcl-Type1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .bwp-Id: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .referenceSignal:- csi-rs: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .qcl-Type: 0 ( typeA)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceAllocation: 0 ( resourceAllocationType0)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pdsch-TimeDomainAllocationList:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .setup [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .mappingType: 0 ( typeA)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startSymbolAndLength: 40
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .setup [ 1 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .mappingType: 0 ( typeA)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startSymbolAndLength: 96
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .rbg-Size: 0 ( config1)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .mcs-Table: 0 ( qam256)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .maxNrofCodeWordsScheduledByDCI: 0 ( n1)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .prb-BundlingType:- staticBundling
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .bundleSize: 0 ( n4)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .zp-CSI-RS-ResourceToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .zp-CSI-RS-ResourceId: 12
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceMapping
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .frequencyDomainAllocation:- other: 8
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofPorts: 2 ( p4)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .firstOFDMSymbolInTimeDomain: 3
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .cdm-Type: 1 ( fd_CDM2)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .density:- one: null
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .freqBand
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startingRB: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofRBs: 276
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .periodicityAndOffset:- slots40: 18
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .zp-CSI-RS-ResourceToAddModList [ 1 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .zp-CSI-RS-ResourceId: 13
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceMapping
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .frequencyDomainAllocation:- other: 15
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofPorts: 7 ( p32)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .firstOFDMSymbolInTimeDomain: 5
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .firstOFDMSymbolInTimeDomain2: 7
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .cdm-Type: 1 ( fd_CDM2)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .density:- one: null
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .freqBand
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startingRB: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofRBs: 276
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .periodicityAndOffset:- slots40: 8
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .p-ZP-CSI-RS-ResourceSet:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .zp-CSI-RS-ResourceSetId: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .zp-CSI-RS-ResourceIdList [ 0 ]: 12
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .zp-CSI-RS-ResourceIdList [ 1 ]: 13
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .radioLinkMonitoringConfig:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .failureDetectionResourcesToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .radioLinkMonitoringRS-Id: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .purpose: 1 ( rlf)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .detectionResource:- ssb-Index: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .firstActiveDownlinkBWP-Id: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .uplinkConfig
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .initialUplinkBWP
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pucch-Config:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceSetToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pucch-ResourceSetId: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceList [ 0 ]: 7
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceList [ 1 ]: 8
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceList [ 2 ]: 9
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceList [ 3 ]: 10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceList [ 4 ]: 11
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceList [ 5 ]: 12
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceList [ 6 ]: 13
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceList [ 7 ]: 14
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceSetToAddModList [ 1 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pucch-ResourceSetId: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceList [ 0 ]: 16
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceList [ 1 ]: 17
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pucch-ResourceId: 7
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startingPRB: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .intraSlotFrequencyHopping: 0 ( enabled)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .secondHopPRB: 272
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .format:- format1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .initialCyclicShift: 2
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofSymbols: 14
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startingSymbolIndex: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .timeDomainOCC: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceToAddModList [ 1 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pucch-ResourceId: 8
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startingPRB: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .intraSlotFrequencyHopping: 0 ( enabled)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .secondHopPRB: 272
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .format:- format1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .initialCyclicShift: 4
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofSymbols: 14
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startingSymbolIndex: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .timeDomainOCC: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceToAddModList [ 2 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pucch-ResourceId: 9
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startingPRB: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .intraSlotFrequencyHopping: 0 ( enabled)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .secondHopPRB: 272
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .format:- format1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .initialCyclicShift: 6
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofSymbols: 14
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startingSymbolIndex: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .timeDomainOCC: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceToAddModList [ 3 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pucch-ResourceId: 10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startingPRB: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .intraSlotFrequencyHopping: 0 ( enabled)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .secondHopPRB: 272
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .format:- format1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .initialCyclicShift: 8
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofSymbols: 14
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startingSymbolIndex: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .timeDomainOCC: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceToAddModList [ 4 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pucch-ResourceId: 11
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startingPRB: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .intraSlotFrequencyHopping: 0 ( enabled)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .secondHopPRB: 272
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .format:- format1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .initialCyclicShift: 10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofSymbols: 14
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startingSymbolIndex: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .timeDomainOCC: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceToAddModList [ 5 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pucch-ResourceId: 12
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startingPRB: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .intraSlotFrequencyHopping: 0 ( enabled)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .secondHopPRB: 272
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .format:- format1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .initialCyclicShift: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofSymbols: 14
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startingSymbolIndex: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .timeDomainOCC: 2
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceToAddModList [ 6 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pucch-ResourceId: 13
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startingPRB: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .intraSlotFrequencyHopping: 0 ( enabled)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .secondHopPRB: 272
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .format:- format1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .initialCyclicShift: 2
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofSymbols: 14
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startingSymbolIndex: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .timeDomainOCC: 2
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceToAddModList [ 7 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pucch-ResourceId: 14
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startingPRB: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .intraSlotFrequencyHopping: 0 ( enabled)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .secondHopPRB: 272
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .format:- format1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .initialCyclicShift: 4
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofSymbols: 14
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startingSymbolIndex: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .timeDomainOCC: 2
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceToAddModList [ 8 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pucch-ResourceId: 31
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startingPRB: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .intraSlotFrequencyHopping: 0 ( enabled)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .secondHopPRB: 272
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .format:- format1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .initialCyclicShift: 8
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofSymbols: 14
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startingSymbolIndex: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .timeDomainOCC: 2
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceToAddModList [ 9 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pucch-ResourceId: 16
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startingPRB: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .intraSlotFrequencyHopping: 0 ( enabled)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .secondHopPRB: 271
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .format:- format3
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofPRBs: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofSymbols: 14
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startingSymbolIndex: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceToAddModList [ 10 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pucch-ResourceId: 17
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startingPRB: 271
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .intraSlotFrequencyHopping: 0 ( enabled)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .secondHopPRB: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .format:- format3
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofPRBs: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofSymbols: 14
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startingSymbolIndex: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .format1:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .format3:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .additionalDMRS: 0 ( true)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .maxCodeRate: 0 ( zeroDot08)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .schedulingRequestResourceToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .schedulingRequestResourceId: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .schedulingRequestID: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .periodicityAndOffset:- sl10: 4
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resource: 31
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .dl-DataToUL-ACK [ 0 ]: 3
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .dl-DataToUL-ACK [ 1 ]: 4
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .dl-DataToUL-ACK [ 2 ]: 6
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .dl-DataToUL-ACK [ 3 ]: 7
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .dl-DataToUL-ACK [ 4 ]: 8
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .dl-DataToUL-ACK [ 5 ]: 9
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .dl-DataToUL-ACK [ 6 ]: 9
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .dl-DataToUL-ACK [ 7 ]: 9
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pusch-Config:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .txConfig: 0 ( codebook)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .dmrs-UplinkForPUSCH-MappingTypeA:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .dmrs-AdditionalPosition: 1 ( pos1)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .transformPrecodingDisabled
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .transformPrecodingEnabled
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pusch-PowerControl
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .p0-AlphaSets [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .p0-PUSCH-AlphaSetId: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .p0: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .alpha: 7 ( alpha1)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceAllocation: 1 ( resourceAllocationType1)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pusch-TimeDomainAllocationList:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .setup [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .k2: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .mappingType: 0 ( typeA)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startSymbolAndLength: 27
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .setup [ 1 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .k2: 2
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .mappingType: 0 ( typeA)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startSymbolAndLength: 27
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .setup [ 2 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .k2: 3
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .mappingType: 0 ( typeA)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startSymbolAndLength: 27
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .setup [ 3 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .k2: 4
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .mappingType: 0 ( typeA)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startSymbolAndLength: 27
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .setup [ 4 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .k2: 5
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .mappingType: 0 ( typeA)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startSymbolAndLength: 27
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .setup [ 5 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .k2: 6
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .mappingType: 0 ( typeA)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startSymbolAndLength: 27
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .transformPrecoder: 1 ( disabled)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .codebookSubset: 2 ( nonCoherent)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .maxRank: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .uci-OnPUSCH:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .betaOffsets:- semiStatic
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .betaOffsetACK-Index1: 8
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .betaOffsetACK-Index2: 10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .betaOffsetACK-Index3: 7
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .betaOffsetCSI-Part1-Index1: 7
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .betaOffsetCSI-Part1-Index2: 6
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .betaOffsetCSI-Part2-Index1: 5
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .betaOffsetCSI-Part2-Index2: 4
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .scaling: 3 ( f1)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .srs-Config:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .srs-ResourceSetToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .srs-ResourceSetId: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .srs-ResourceIdList [ 0 ]: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceType:- aperiodic
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .aperiodicSRS-ResourceTrigger: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .usage: 1 ( codebook)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .p0: -110
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .srs-ResourceToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .srs-ResourceId: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofSRS-Ports: 0 ( port1)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .transmissionComb:- n2
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .combOffset-n2: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .cyclicShift-n2: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceMapping
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startPosition: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofSymbols: 0 ( n1)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .repetitionFactor: 0 ( n1)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .freqDomainPosition: 4
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .freqDomainShift: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .freqHopping
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .c-SRS: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .b-SRS: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .b-hop: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .groupOrSequenceHopping: 0 ( neither)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceType:- aperiodic
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .sequenceId: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .firstActiveUplinkBWP-Id: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pusch-ServingCellConfig:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pdsch-ServingCellConfig:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofHARQ-ProcessesForPDSCH: 5 ( n16)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .csi-MeasConfig:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nzp-CSI-RS-ResourceToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nzp-CSI-RS-ResourceId: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceMapping
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .frequencyDomainAllocation:- row1: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofPorts: 0 ( p1)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .firstOFDMSymbolInTimeDomain: 4
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .cdm-Type: 0 ( noCDM)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .density:- three: null
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .freqBand
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startingRB: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofRBs: 276
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .powerControlOffset: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .scramblingID: 909
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .periodicityAndOffset:- slots80: 16
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .qcl-InfoPeriodicCSI-RS: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nzp-CSI-RS-ResourceToAddModList [ 1 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nzp-CSI-RS-ResourceId: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceMapping
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .frequencyDomainAllocation:- row1: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofPorts: 0 ( p1)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .firstOFDMSymbolInTimeDomain: 8
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .cdm-Type: 0 ( noCDM)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .density:- three: null
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .freqBand
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startingRB: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofRBs: 276
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .powerControlOffset: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .scramblingID: 909
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .periodicityAndOffset:- slots80: 16
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .qcl-InfoPeriodicCSI-RS: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nzp-CSI-RS-ResourceToAddModList [ 2 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nzp-CSI-RS-ResourceId: 2
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceMapping
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .frequencyDomainAllocation:- row1: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofPorts: 0 ( p1)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .firstOFDMSymbolInTimeDomain: 4
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .cdm-Type: 0 ( noCDM)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .density:- three: null
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .freqBand
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startingRB: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofRBs: 276
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .powerControlOffset: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .scramblingID: 909
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .periodicityAndOffset:- slots80: 17
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .qcl-InfoPeriodicCSI-RS: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nzp-CSI-RS-ResourceToAddModList [ 3 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nzp-CSI-RS-ResourceId: 3
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceMapping
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .frequencyDomainAllocation:- row1: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofPorts: 0 ( p1)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .firstOFDMSymbolInTimeDomain: 8
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .cdm-Type: 0 ( noCDM)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .density:- three: null
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .freqBand
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startingRB: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofRBs: 276
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .powerControlOffset: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .scramblingID: 909
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .periodicityAndOffset:- slots80: 17
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .qcl-InfoPeriodicCSI-RS: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nzp-CSI-RS-ResourceToAddModList [ 4 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nzp-CSI-RS-ResourceId: 4
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceMapping
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .frequencyDomainAllocation:- other: 15
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofPorts: 3 ( p8)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .firstOFDMSymbolInTimeDomain: 5
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .cdm-Type: 1 ( fd_CDM2)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .density:- one: null
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .freqBand
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startingRB: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofRBs: 276
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .powerControlOffset: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .scramblingID: 909
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .periodicityAndOffset:- slots40: 18
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .qcl-InfoPeriodicCSI-RS: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nzp-CSI-RS-ResourceSetToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nzp-CSI-ResourceSetId: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nzp-CSI-RS-Resources [ 0 ]: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nzp-CSI-RS-Resources [ 1 ]: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nzp-CSI-RS-Resources [ 2 ]: 2
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nzp-CSI-RS-Resources [ 3 ]: 3
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .trs-Info: 0 ( true)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nzp-CSI-RS-ResourceSetToAddModList [ 1 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nzp-CSI-ResourceSetId: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nzp-CSI-RS-Resources [ 0 ]: 4
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .csi-IM-ResourceToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .csi-IM-ResourceId: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .csi-IM-ResourceElementPattern:- pattern0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .subcarrierLocation-p0: 3 ( s6)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .symbolLocation-p0: 3
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .freqBand
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .startingRB: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofRBs: 276
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .periodicityAndOffset:- slots40: 18
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .csi-IM-ResourceSetToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .csi-IM-ResourceSetId: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .csi-IM-Resources [ 0 ]: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .csi-ResourceConfigToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .csi-ResourceConfigId: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .csi-RS-ResourceSetList:- nzp-CSI-RS-SSB
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nzp-CSI-RS-ResourceSetList [ 0 ]: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .bwp-Id: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceType: 2 ( periodic)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .csi-ResourceConfigToAddModList [ 1 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .csi-ResourceConfigId: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .csi-RS-ResourceSetList:- nzp-CSI-RS-SSB
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nzp-CSI-RS-ResourceSetList [ 0 ]: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .bwp-Id: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceType: 2 ( periodic)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .csi-ResourceConfigToAddModList [ 2 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .csi-ResourceConfigId: 3
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .csi-RS-ResourceSetList:- csi-IM-ResourceSetList
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .csi-IM-ResourceSetList [ 0 ]: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .bwp-Id: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceType: 2 ( periodic)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .csi-ReportConfigToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .reportConfigId: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourcesForChannelMeasurement: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .csi-IM-ResourcesForInterference: 3
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .reportConfigType:- aperiodic
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .reportSlotOffsetList [ 0 ]: 6
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .reportSlotOffsetList [ 1 ]: 6
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .reportSlotOffsetList [ 2 ]: 6
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .reportSlotOffsetList [ 3 ]: 6
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .reportSlotOffsetList [ 4 ]: 6
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .reportSlotOffsetList [ 5 ]: 6
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .reportSlotOffsetList [ 6 ]: 6
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .reportSlotOffsetList [ 7 ]: 6
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .reportQuantity:- cri-RI-PMI-CQI: null
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .reportFreqConfiguration
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .cqi-FormatIndicator: 0 ( widebandCQI)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pmi-FormatIndicator: 0 ( widebandPMI)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .csi-ReportingBand:- subbands9: 511
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .timeRestrictionForChannelMeasurements: 1 ( notConfigured)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .timeRestrictionForInterferenceMeasurements: 1 ( notConfigured)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .codebookConfig
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .codebookType:- type1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .subType:- typeI-SinglePanel
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrOfAntennaPorts:- moreThanTwo
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .n1-n2:- four-one-TypeI-SinglePanel-Restriction: 65535
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .typeI-SinglePanel-ri-Restriction: 15
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .codebookMode: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .dummy: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .groupBasedBeamReporting:- disabled
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nrofReportedRS: 0 ( n1)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .cqi-Table: 1 ( table2)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .subbandSize: 1 ( value2)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .reportTriggerSize: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .aperiodicTriggerStateList:- setup
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .setup [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .associatedReportConfigInfoList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .reportConfigId: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourcesForChannel:- nzp-CSI-RS
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .resourceSet: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .csi-IM-ResourcesForInterference: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .tag-Id: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .servingCellMO: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .measConfig
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .measObjectToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .measObjectId: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .measObject:- measObjectNR
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .ssbFrequency: 633696
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .ssbSubcarrierSpacing: 1 ( kHz30)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .smtc1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .periodicityAndOffset:- sf20: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .duration: 0 ( sf1)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .referenceSignalConfig
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .ssb-ConfigMobility
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .deriveSSB-IndexFromCell: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .quantityConfigIndex: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .offsetMO
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .freqBandIndicatorNR: 78
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .reportConfigToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .reportConfigId: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .reportConfig:- reportConfigNR
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .reportType:- eventTriggered
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .eventId:- eventA3
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .a3-Offset:- rsrp: 6 (3.00 dB)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .reportOnLeave: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .hysteresis: 2 (1.00 dB)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .timeToTrigger: 6 ( ms160)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .useWhiteCellList: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .rsType: 0 ( ssb)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .reportInterval: 0 ( ms120)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .reportAmount: 7 ( infinity)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .reportQuantityCell
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .rsrp: 1 (True)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .rsrq: 1 (True)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .sinr: 0 (False)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .maxReportCells: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .includeBeamMeasurements: 0 (False)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .measIdToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .measId: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .measObjectId: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .reportConfigId: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .s-MeasureConfig:- ssb-RSRP: 127 (-30.00 dBm)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .quantityConfig
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .quantityConfigNR-List [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .quantityConfigCell
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .ssb-FilterConfig
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .filterCoefficientRSRQ: 10 ( fc11)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .csi-RS-FilterConfig
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .filterCoefficientRSRQ: 10 ( fc11)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .---EMBEDDED CONTAINER DECODING END---
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .p-MaxEUTRA-r15: 20 (20.0 dBm)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .sk-Counter-r15: 0
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .nr-RadioBearerConfig2-r15: 0x1409289f8ec5374d83
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .---EMBEDDED CONTAINER DECODING START---
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .NR_Uu_RRC: 
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .RadioBearerConfig
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .drb-ToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .cnAssociation:- eps-BearerIdentity: 5
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .drb-Identity: 3
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pdcp-Config
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .drb
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .discardTimer: 14 ( ms1500)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pdcp-SN-SizeUL: 1 ( len18bits)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .pdcp-SN-SizeDL: 1 ( len18bits)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .headerCompression:- notUsed: null
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .moreThanOneRLC
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .primaryPath
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .cellGroup: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .ul-DataSplitThreshold: 23 ( infinity)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .t-Reordering: 19 ( ms200)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .securityConfig
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .securityAlgorithmConfig
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .cipheringAlgorithm: 1 ( nea1)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .keyToUse: 1 ( secondary)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .---EMBEDDED CONTAINER DECODING END---


'''
a = '''
000439 06:23:00.115  {A L3M DL DCCH: 5}  DL-DCCH RRCConnectionReconfiguration
  
Release: 16, 
Version: 16, 
RB Id: 1, 
PCI: 169, 
EARFCN: 00400, 
Chan Type: 5, 
Msg Type: 4, 
Msg Name: RRCConnectionReconfiguration, 
Msg Body: 26103FC082310C01400C852F00152F20C00E754BC040640A300C4E32F01019030C017D54BC040640A5518E849C08A212063C0A02802023E2B4101811B15A081008B8AD040288A92DEDC0A0280B10003102B1BB60325141D8349AF165818E84A96C6B9E80000200860190040803122E455CCCCA01A8CC6A28
LTE_Uu_RRC: DL_DCCH_Message
-   .   .message:- c1:- rrcConnectionReconfiguration
-   .   .   .   .   .rrc-TransactionIdentifier: 3
-   .   .   .   .   .criticalExtensions:- c1:- rrcConnectionReconfiguration-r8
-   .   .   .   .   .   .   .   .measConfig
-   .   .   .   .   .   .   .   .   .measObjectToRemoveList [ 0 ]: 2
-   .   .   .   .   .   .   .   .   .measObjectToRemoveList [ 1 ]: 4
-   .   .   .   .   .   .   .   .   .measObjectToRemoveList [ 2 ]: 3
-   .   .   .   .   .   .   .   .   .measObjectToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .measObjectId: 1
-   .   .   .   .   .   .   .   .   .   .measObject:- measObjectEUTRA
-   .   .   .   .   .   .   .   .   .   .   .   .carrierFreq: 400
-   .   .   .   .   .   .   .   .   .   .   .   .allowedMeasBandwidth: 5 ( mbw100)
-   .   .   .   .   .   .   .   .   .   .   .   .presenceAntennaPort1: 0 (False)
-   .   .   .   .   .   .   .   .   .   .   .   .neighCellConfig: 1
-   .   .   .   .   .   .   .   .   .   .   .   .offsetFreq: 15 ( dB0)
-   .   .   .   .   .   .   .   .   .   .   .   .cellsToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .cellIndex: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .physCellId: 169
-   .   .   .   .   .   .   .   .   .   .   .   .   .cellIndividualOffset: 15 ( dB0)
-   .   .   .   .   .   .   .   .   .measObjectToAddModList [ 1 ]
-   .   .   .   .   .   .   .   .   .   .measObjectId: 5
-   .   .   .   .   .   .   .   .   .   .measObject:- measObjectEUTRA
-   .   .   .   .   .   .   .   .   .   .   .   .carrierFreq: 1850
-   .   .   .   .   .   .   .   .   .   .   .   .allowedMeasBandwidth: 5 ( mbw100)
-   .   .   .   .   .   .   .   .   .   .   .   .presenceAntennaPort1: 0 (False)
-   .   .   .   .   .   .   .   .   .   .   .   .neighCellConfig: 1
-   .   .   .   .   .   .   .   .   .   .   .   .offsetFreq: 15 ( dB0)
-   .   .   .   .   .   .   .   .   .   .   .   .measCycleSCell-r10: 2
-   .   .   .   .   .   .   .   .   .measObjectToAddModList [ 2 ]
-   .   .   .   .   .   .   .   .   .   .measObjectId: 6
-   .   .   .   .   .   .   .   .   .   .measObject:- measObjectEUTRA
-   .   .   .   .   .   .   .   .   .   .   .   .carrierFreq: 6300
-   .   .   .   .   .   .   .   .   .   .   .   .allowedMeasBandwidth: 3 ( mbw50)
-   .   .   .   .   .   .   .   .   .   .   .   .presenceAntennaPort1: 0 (False)
-   .   .   .   .   .   .   .   .   .   .   .   .neighCellConfig: 1
-   .   .   .   .   .   .   .   .   .   .   .   .offsetFreq: 15 ( dB0)
-   .   .   .   .   .   .   .   .   .   .   .   .measCycleSCell-r10: 2
-   .   .   .   .   .   .   .   .   .measObjectToAddModList [ 3 ]
-   .   .   .   .   .   .   .   .   .   .measObjectId: 7
-   .   .   .   .   .   .   .   .   .   .measObject:- measObjectEUTRA
-   .   .   .   .   .   .   .   .   .   .   .   .carrierFreq: 3050
-   .   .   .   .   .   .   .   .   .   .   .   .allowedMeasBandwidth: 5 ( mbw100)
-   .   .   .   .   .   .   .   .   .   .   .   .presenceAntennaPort1: 0 (False)
-   .   .   .   .   .   .   .   .   .   .   .   .neighCellConfig: 1
-   .   .   .   .   .   .   .   .   .   .   .   .offsetFreq: 15 ( dB0)
-   .   .   .   .   .   .   .   .   .   .   .   .measCycleSCell-r10: 2
-   .   .   .   .   .   .   .   .   .reportConfigToRemoveList [ 0 ]: 6
-   .   .   .   .   .   .   .   .   .reportConfigToRemoveList [ 1 ]: 11
-   .   .   .   .   .   .   .   .   .reportConfigToRemoveList [ 2 ]: 7
-   .   .   .   .   .   .   .   .   .reportConfigToRemoveList [ 3 ]: 8
-   .   .   .   .   .   .   .   .   .reportConfigToRemoveList [ 4 ]: 9
-   .   .   .   .   .   .   .   .   .reportConfigToRemoveList [ 5 ]: 10
-   .   .   .   .   .   .   .   .   .reportConfigToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 1
-   .   .   .   .   .   .   .   .   .   .reportConfig:- reportConfigEUTRA
-   .   .   .   .   .   .   .   .   .   .   .   .triggerType:- event
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .eventId:- eventA3
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .a3-Offset: 4 (2.0 dB)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .reportOnLeave: 0 (False)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .hysteresis: 4 (2.0 dB)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .timeToTrigger: 8 ( ms320)
-   .   .   .   .   .   .   .   .   .   .   .   .triggerQuantity: 0 ( rsrp)
-   .   .   .   .   .   .   .   .   .   .   .   .reportQuantity: 0 ( sameAsTriggerQuantity)
-   .   .   .   .   .   .   .   .   .   .   .   .maxReportCells: 4
-   .   .   .   .   .   .   .   .   .   .   .   .reportInterval: 1 ( ms240)
-   .   .   .   .   .   .   .   .   .   .   .   .reportAmount: 7 ( infinity)
-   .   .   .   .   .   .   .   .   .   .   .   .reportAddNeighMeas-r10: 0
-   .   .   .   .   .   .   .   .   .reportConfigToAddModList [ 1 ]
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 3
-   .   .   .   .   .   .   .   .   .   .reportConfig:- reportConfigEUTRA
-   .   .   .   .   .   .   .   .   .   .   .   .triggerType:- event
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .eventId:- eventA2
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .a2-Threshold:- threshold-RSRP: 31 (-109.00 dBm)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .hysteresis: 2 (1.0 dB)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .timeToTrigger: 11 ( ms640)
-   .   .   .   .   .   .   .   .   .   .   .   .triggerQuantity: 0 ( rsrp)
-   .   .   .   .   .   .   .   .   .   .   .   .reportQuantity: 1 ( both)
-   .   .   .   .   .   .   .   .   .   .   .   .maxReportCells: 1
-   .   .   .   .   .   .   .   .   .   .   .   .reportInterval: 2 ( ms480)
-   .   .   .   .   .   .   .   .   .   .   .   .reportAmount: 0 ( r1)
-   .   .   .   .   .   .   .   .   .reportConfigToAddModList [ 2 ]
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 4
-   .   .   .   .   .   .   .   .   .   .reportConfig:- reportConfigEUTRA
-   .   .   .   .   .   .   .   .   .   .   .   .triggerType:- event
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .eventId:- eventA2
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .a2-Threshold:- threshold-RSRP: 27 (-113.00 dBm)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .hysteresis: 2 (1.0 dB)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .timeToTrigger: 11 ( ms640)
-   .   .   .   .   .   .   .   .   .   .   .   .triggerQuantity: 0 ( rsrp)
-   .   .   .   .   .   .   .   .   .   .   .   .reportQuantity: 1 ( both)
-   .   .   .   .   .   .   .   .   .   .   .   .maxReportCells: 1
-   .   .   .   .   .   .   .   .   .   .   .   .reportInterval: 2 ( ms480)
-   .   .   .   .   .   .   .   .   .   .   .   .reportAmount: 0 ( r1)
-   .   .   .   .   .   .   .   .   .reportConfigToAddModList [ 3 ]
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 5
-   .   .   .   .   .   .   .   .   .   .reportConfig:- reportConfigEUTRA
-   .   .   .   .   .   .   .   .   .   .   .   .triggerType:- event
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .eventId:- eventA2
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .a2-Threshold:- threshold-RSRP: 23 (-117.00 dBm)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .hysteresis: 2 (1.0 dB)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .timeToTrigger: 11 ( ms640)
-   .   .   .   .   .   .   .   .   .   .   .   .triggerQuantity: 0 ( rsrp)
-   .   .   .   .   .   .   .   .   .   .   .   .reportQuantity: 1 ( both)
-   .   .   .   .   .   .   .   .   .   .   .   .maxReportCells: 1
-   .   .   .   .   .   .   .   .   .   .   .   .reportInterval: 2 ( ms480)
-   .   .   .   .   .   .   .   .   .   .   .   .reportAmount: 0 ( r1)
-   .   .   .   .   .   .   .   .   .reportConfigToAddModList [ 4 ]
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 2
-   .   .   .   .   .   .   .   .   .   .reportConfig:- reportConfigEUTRA
-   .   .   .   .   .   .   .   .   .   .   .   .triggerType:- event
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .eventId:- eventA3
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .a3-Offset: -20 (-10.0 dB)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .reportOnLeave: 1 (True)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .hysteresis: 4 (2.0 dB)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .timeToTrigger: 11 ( ms640)
-   .   .   .   .   .   .   .   .   .   .   .   .triggerQuantity: 0 ( rsrp)
-   .   .   .   .   .   .   .   .   .   .   .   .reportQuantity: 1 ( both)
-   .   .   .   .   .   .   .   .   .   .   .   .maxReportCells: 8
-   .   .   .   .   .   .   .   .   .   .   .   .reportInterval: 6 ( ms5120)
-   .   .   .   .   .   .   .   .   .   .   .   .reportAmount: 7 ( infinity)
-   .   .   .   .   .   .   .   .   .   .   .   .reportAddNeighMeas-r10: 0
-   .   .   .   .   .   .   .   .   .reportConfigToAddModList [ 5 ]
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 12
-   .   .   .   .   .   .   .   .   .   .reportConfig:- reportConfigEUTRA
-   .   .   .   .   .   .   .   .   .   .   .   .triggerType:- event
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .eventId:- eventA6-r10
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .a6-Offset-r10: 4 (2.0 dB)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .a6-ReportOnLeave-r10: 0 (False)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .hysteresis: 2 (1.0 dB)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .timeToTrigger: 11 ( ms640)
-   .   .   .   .   .   .   .   .   .   .   .   .triggerQuantity: 0 ( rsrp)
-   .   .   .   .   .   .   .   .   .   .   .   .reportQuantity: 0 ( sameAsTriggerQuantity)
-   .   .   .   .   .   .   .   .   .   .   .   .maxReportCells: 4
-   .   .   .   .   .   .   .   .   .   .   .   .reportInterval: 7 ( ms10240)
-   .   .   .   .   .   .   .   .   .   .   .   .reportAmount: 3 ( r8)
-   .   .   .   .   .   .   .   .   .reportConfigToAddModList [ 6 ]
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 13
-   .   .   .   .   .   .   .   .   .   .reportConfig:- reportConfigEUTRA
-   .   .   .   .   .   .   .   .   .   .   .   .triggerType:- event
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .eventId:- eventA4
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .a4-Threshold:- threshold-RSRP: 37 (-103.00 dBm)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .hysteresis: 2 (1.0 dB)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .timeToTrigger: 8 ( ms320)
-   .   .   .   .   .   .   .   .   .   .   .   .triggerQuantity: 0 ( rsrp)
-   .   .   .   .   .   .   .   .   .   .   .   .reportQuantity: 0 ( sameAsTriggerQuantity)
-   .   .   .   .   .   .   .   .   .   .   .   .maxReportCells: 8
-   .   .   .   .   .   .   .   .   .   .   .   .reportInterval: 6 ( ms5120)
-   .   .   .   .   .   .   .   .   .   .   .   .reportAmount: 0 ( r1)
-   .   .   .   .   .   .   .   .   .reportConfigToAddModList [ 7 ]
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 14
-   .   .   .   .   .   .   .   .   .   .reportConfig:- reportConfigEUTRA
-   .   .   .   .   .   .   .   .   .   .   .   .triggerType:- periodical
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .purpose: 0 ( reportStrongestCells)
-   .   .   .   .   .   .   .   .   .   .   .   .triggerQuantity: 0 ( rsrp)
-   .   .   .   .   .   .   .   .   .   .   .   .reportQuantity: 1 ( both)
-   .   .   .   .   .   .   .   .   .   .   .   .maxReportCells: 6
-   .   .   .   .   .   .   .   .   .   .   .   .reportInterval: 7 ( ms10240)
-   .   .   .   .   .   .   .   .   .   .   .   .reportAmount: 4 ( r16)
-   .   .   .   .   .   .   .   .   .measIdToRemoveList [ 0 ]: 6
-   .   .   .   .   .   .   .   .   .measIdToRemoveList [ 1 ]: 17
-   .   .   .   .   .   .   .   .   .measIdToRemoveList [ 2 ]: 7
-   .   .   .   .   .   .   .   .   .measIdToRemoveList [ 3 ]: 8
-   .   .   .   .   .   .   .   .   .measIdToRemoveList [ 4 ]: 9
-   .   .   .   .   .   .   .   .   .measIdToRemoveList [ 5 ]: 10
-   .   .   .   .   .   .   .   .   .measIdToRemoveList [ 6 ]: 11
-   .   .   .   .   .   .   .   .   .measIdToRemoveList [ 7 ]: 12
-   .   .   .   .   .   .   .   .   .measIdToRemoveList [ 8 ]: 13
-   .   .   .   .   .   .   .   .   .measIdToRemoveList [ 9 ]: 14
-   .   .   .   .   .   .   .   .   .measIdToRemoveList [ 10 ]: 15
-   .   .   .   .   .   .   .   .   .measIdToRemoveList [ 11 ]: 16
-   .   .   .   .   .   .   .   .   .measIdToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .measId: 1
-   .   .   .   .   .   .   .   .   .   .measObjectId: 1
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 1
-   .   .   .   .   .   .   .   .   .measIdToAddModList [ 1 ]
-   .   .   .   .   .   .   .   .   .   .measId: 3
-   .   .   .   .   .   .   .   .   .   .measObjectId: 1
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 3
-   .   .   .   .   .   .   .   .   .measIdToAddModList [ 2 ]
-   .   .   .   .   .   .   .   .   .   .measId: 4
-   .   .   .   .   .   .   .   .   .   .measObjectId: 1
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 4
-   .   .   .   .   .   .   .   .   .measIdToAddModList [ 3 ]
-   .   .   .   .   .   .   .   .   .   .measId: 5
-   .   .   .   .   .   .   .   .   .   .measObjectId: 1
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 5
-   .   .   .   .   .   .   .   .   .measIdToAddModList [ 4 ]
-   .   .   .   .   .   .   .   .   .   .measId: 2
-   .   .   .   .   .   .   .   .   .   .measObjectId: 1
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 2
-   .   .   .   .   .   .   .   .   .measIdToAddModList [ 5 ]
-   .   .   .   .   .   .   .   .   .   .measId: 18
-   .   .   .   .   .   .   .   .   .   .measObjectId: 5
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 12
-   .   .   .   .   .   .   .   .   .measIdToAddModList [ 6 ]
-   .   .   .   .   .   .   .   .   .   .measId: 19
-   .   .   .   .   .   .   .   .   .   .measObjectId: 6
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 12
-   .   .   .   .   .   .   .   .   .measIdToAddModList [ 7 ]
-   .   .   .   .   .   .   .   .   .   .measId: 20
-   .   .   .   .   .   .   .   .   .   .measObjectId: 7
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 13
-   .   .   .   .   .   .   .   .   .measIdToAddModList [ 8 ]
-   .   .   .   .   .   .   .   .   .   .measId: 21
-   .   .   .   .   .   .   .   .   .   .measObjectId: 1
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 14
-   .   .   .   .   .   .   .   .   .quantityConfig
-   .   .   .   .   .   .   .   .   .   .quantityConfigEUTRA
-   .   .   .   .   .   .   .   .   .   .   .filterCoefficientRSRP: 6 ( fc6)
-   .   .   .   .   .   .   .   .   .   .   .filterCoefficientRSRQ: 6 ( fc6)
-   .   .   .   .   .   .   .   .   .measGapConfig:- setup
-   .   .   .   .   .   .   .   .   .   .   .gapOffset:- gp1: 10
'''

b = '''
000360 06:22:59.494  {A L3M DL DCCH: 5}  DL-DCCH RRCConnectionReconfiguration
  
Release: 16, 
Version: 16, 
RB Id: 1, 
PCI: 169, 
EARFCN: 06300, 
Chan Type: 5, 
Msg Type: 4, 
Msg Name: RRCConnectionReconfiguration, 
Msg Body: 20101500C23005F552F01019018C00E754BC04064043000C852F01019000503138CBC0054BC4848C2482B18F0280A025262C42B98F0280A0280948AC020CA0A163430486852E1A5E24C00A
LTE_Uu_RRC: DL_DCCH_Message
-   .   .message:- c1:- rrcConnectionReconfiguration
-   .   .   .   .   .rrc-TransactionIdentifier: 0
-   .   .   .   .   .criticalExtensions:- c1:- rrcConnectionReconfiguration-r8
-   .   .   .   .   .   .   .   .measConfig
-   .   .   .   .   .   .   .   .   .measObjectToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .measObjectId: 2
-   .   .   .   .   .   .   .   .   .   .measObject:- measObjectEUTRA
-   .   .   .   .   .   .   .   .   .   .   .   .carrierFreq: 3050
-   .   .   .   .   .   .   .   .   .   .   .   .allowedMeasBandwidth: 5 ( mbw100)
-   .   .   .   .   .   .   .   .   .   .   .   .presenceAntennaPort1: 0 (False)
-   .   .   .   .   .   .   .   .   .   .   .   .neighCellConfig: 1
-   .   .   .   .   .   .   .   .   .   .   .   .offsetFreq: 15 ( dB0)
-   .   .   .   .   .   .   .   .   .   .   .   .measCycleSCell-r10: 2
-   .   .   .   .   .   .   .   .   .measObjectToAddModList [ 1 ]
-   .   .   .   .   .   .   .   .   .   .measObjectId: 4
-   .   .   .   .   .   .   .   .   .   .measObject:- measObjectEUTRA
-   .   .   .   .   .   .   .   .   .   .   .   .carrierFreq: 1850
-   .   .   .   .   .   .   .   .   .   .   .   .allowedMeasBandwidth: 5 ( mbw100)
-   .   .   .   .   .   .   .   .   .   .   .   .presenceAntennaPort1: 0 (False)
-   .   .   .   .   .   .   .   .   .   .   .   .neighCellConfig: 1
-   .   .   .   .   .   .   .   .   .   .   .   .offsetFreq: 15 ( dB0)
-   .   .   .   .   .   .   .   .   .   .   .   .measCycleSCell-r10: 2
-   .   .   .   .   .   .   .   .   .measObjectToAddModList [ 2 ]
-   .   .   .   .   .   .   .   .   .   .measObjectId: 3
-   .   .   .   .   .   .   .   .   .   .measObject:- measObjectEUTRA
-   .   .   .   .   .   .   .   .   .   .   .   .carrierFreq: 400
-   .   .   .   .   .   .   .   .   .   .   .   .allowedMeasBandwidth: 5 ( mbw100)
-   .   .   .   .   .   .   .   .   .   .   .   .presenceAntennaPort1: 0 (False)
-   .   .   .   .   .   .   .   .   .   .   .   .neighCellConfig: 1
-   .   .   .   .   .   .   .   .   .   .   .   .offsetFreq: 15 ( dB0)
-   .   .   .   .   .   .   .   .   .   .   .   .measCycleSCell-r10: 2
-   .   .   .   .   .   .   .   .   .measObjectToAddModList [ 3 ]
-   .   .   .   .   .   .   .   .   .   .measObjectId: 1
-   .   .   .   .   .   .   .   .   .   .measObject:- measObjectEUTRA
-   .   .   .   .   .   .   .   .   .   .   .   .carrierFreq: 6300
-   .   .   .   .   .   .   .   .   .   .   .   .allowedMeasBandwidth: 3 ( mbw50)
-   .   .   .   .   .   .   .   .   .   .   .   .presenceAntennaPort1: 0 (False)
-   .   .   .   .   .   .   .   .   .   .   .   .neighCellConfig: 1
-   .   .   .   .   .   .   .   .   .   .   .   .offsetFreq: 15 ( dB0)
-   .   .   .   .   .   .   .   .   .   .   .   .cellsToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .   .   .   .cellIndex: 1
-   .   .   .   .   .   .   .   .   .   .   .   .   .physCellId: 169
-   .   .   .   .   .   .   .   .   .   .   .   .   .cellIndividualOffset: 15 ( dB0)
-   .   .   .   .   .   .   .   .   .reportConfigToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 9
-   .   .   .   .   .   .   .   .   .   .reportConfig:- reportConfigEUTRA
-   .   .   .   .   .   .   .   .   .   .   .   .triggerType:- event
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .eventId:- eventA5
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .a5-Threshold1:- threshold-RSRP: 97 (-43.00 dBm)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .a5-Threshold2:- threshold-RSRP: 36 (-104.00 dBm)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .hysteresis: 2 (1.0 dB)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .timeToTrigger: 11 ( ms640)
-   .   .   .   .   .   .   .   .   .   .   .   .triggerQuantity: 0 ( rsrp)
-   .   .   .   .   .   .   .   .   .   .   .   .reportQuantity: 0 ( sameAsTriggerQuantity)
-   .   .   .   .   .   .   .   .   .   .   .   .maxReportCells: 4
-   .   .   .   .   .   .   .   .   .   .   .   .reportInterval: 1 ( ms240)
-   .   .   .   .   .   .   .   .   .   .   .   .reportAmount: 7 ( infinity)
-   .   .   .   .   .   .   .   .   .   .   .   .reportAddNeighMeas-r10: 0
-   .   .   .   .   .   .   .   .   .reportConfigToAddModList [ 1 ]
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 10
-   .   .   .   .   .   .   .   .   .   .reportConfig:- reportConfigEUTRA
-   .   .   .   .   .   .   .   .   .   .   .   .triggerType:- event
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .eventId:- eventA5
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .a5-Threshold1:- threshold-RSRQ: 34 (-3.00 dB)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .a5-Threshold2:- threshold-RSRQ: 34 (-3.00 dB)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .hysteresis: 2 (1.0 dB)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .timeToTrigger: 11 ( ms640)
-   .   .   .   .   .   .   .   .   .   .   .   .triggerQuantity: 1 ( rsrq)
-   .   .   .   .   .   .   .   .   .   .   .   .reportQuantity: 0 ( sameAsTriggerQuantity)
-   .   .   .   .   .   .   .   .   .   .   .   .maxReportCells: 4
-   .   .   .   .   .   .   .   .   .   .   .   .reportInterval: 1 ( ms240)
-   .   .   .   .   .   .   .   .   .   .   .   .reportAmount: 7 ( infinity)
-   .   .   .   .   .   .   .   .   .   .   .   .reportAddNeighMeas-r10: 0
-   .   .   .   .   .   .   .   .   .reportConfigToAddModList [ 2 ]
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 11
-   .   .   .   .   .   .   .   .   .   .reportConfig:- reportConfigEUTRA
-   .   .   .   .   .   .   .   .   .   .   .   .triggerType:- event
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .eventId:- eventA2
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .a2-Threshold:- threshold-RSRP: 41 (-99.00 dBm)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .hysteresis: 2 (1.0 dB)
-   .   .   .   .   .   .   .   .   .   .   .   .   .   .timeToTrigger: 11 ( ms640)
-   .   .   .   .   .   .   .   .   .   .   .   .triggerQuantity: 0 ( rsrp)
-   .   .   .   .   .   .   .   .   .   .   .   .reportQuantity: 0 ( sameAsTriggerQuantity)
-   .   .   .   .   .   .   .   .   .   .   .   .maxReportCells: 1
-   .   .   .   .   .   .   .   .   .   .   .   .reportInterval: 1 ( ms240)
-   .   .   .   .   .   .   .   .   .   .   .   .reportAmount: 0 ( r1)
-   .   .   .   .   .   .   .   .   .measIdToAddModList [ 0 ]
-   .   .   .   .   .   .   .   .   .   .measId: 11
-   .   .   .   .   .   .   .   .   .   .measObjectId: 2
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 9
-   .   .   .   .   .   .   .   .   .measIdToAddModList [ 1 ]
-   .   .   .   .   .   .   .   .   .   .measId: 12
-   .   .   .   .   .   .   .   .   .   .measObjectId: 4
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 9
-   .   .   .   .   .   .   .   .   .measIdToAddModList [ 2 ]
-   .   .   .   .   .   .   .   .   .   .measId: 13
-   .   .   .   .   .   .   .   .   .   .measObjectId: 3
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 9
-   .   .   .   .   .   .   .   .   .measIdToAddModList [ 3 ]
-   .   .   .   .   .   .   .   .   .   .measId: 14
-   .   .   .   .   .   .   .   .   .   .measObjectId: 2
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 10
-   .   .   .   .   .   .   .   .   .measIdToAddModList [ 4 ]
-   .   .   .   .   .   .   .   .   .   .measId: 15
-   .   .   .   .   .   .   .   .   .   .measObjectId: 4
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 10
-   .   .   .   .   .   .   .   .   .measIdToAddModList [ 5 ]
-   .   .   .   .   .   .   .   .   .   .measId: 16
-   .   .   .   .   .   .   .   .   .   .measObjectId: 3
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 10
-   .   .   .   .   .   .   .   .   .measIdToAddModList [ 6 ]
-   .   .   .   .   .   .   .   .   .   .measId: 17
-   .   .   .   .   .   .   .   .   .   .measObjectId: 1
-   .   .   .   .   .   .   .   .   .   .reportConfigId: 11
'''

SPLIT_PATTERN = "\n"

def get_information(info_type, info_string):
    '''
        Edge case is that sometimes the 4G and 5G RRC Reconfig are appended together causing report id clashes
    '''
    assert info_type >= 1 and info_type <= 3, "Info_type = 1 means measobjecttoaddmodlist, 2 means reportconfigtoaddmodlist and 3 means measIds"
    info_string = info_string.lower()
    if info_type == 1:
        pattern = r"measobjecttoaddmodlist \[ (\d*) ][\d\W\w]*?reportconfig" #Pattern to get everything in measobjecttoaddmodlist
        neglen = len("reportconfig")
    elif info_type == 2:
        pattern = r"reportconfigtoaddmodlist \[ (\d*) ][\d\W\w]*?measidto" #Pattern for reportConfigToAddModList
        neglen = len("measidto")
    elif info_type == 3:
        pattern_3_initial = r"measidtoaddmodlist \[ (\d*) ][\d\W\w]*?quant" #try this pattern first, else the other
        neglen = len("quant")
        a_s = re.search( pattern_3_initial, info_string )
        if a_s is None:
            pattern = r"measidtoaddmodlist \[ (\d*) ][\d\W\w]*reportconfigid: \d*" #Pattern for measIdtoAddModList
        else:
            return info_string[a_s.span()[0]:a_s.span()[1] - neglen], a_s.span()
            
        neglen = 0

    a_s = re.search( pattern, info_string )
    if a_s is not None:
        return info_string[a_s.span()[0]:a_s.span()[1] - neglen], a_s.span()
    else:
        return None, (-1, -1)
    
def clean_res(cstring):
    '''
        cstring should come from the get_information function which is cleaned and returned
    '''
    temp = cstring.replace(". ", "").replace(" ", "").replace("-.", "")
    temp = temp.lower()
    return temp


def decode_rpt_type(info_type, info_string):
    '''
        Decodes the message into dictionary based on the info_type filter.
    '''
    assert info_type >= 1 and info_type <= 3, "Info_type = 1 means measobjecttoaddmodlist, 2 means reportconfigtoaddmodlist and 3 means measIds"
    info_string = info_string.lower()
    if info_type == 1:
        pattern = r"measobjecttoaddmodlist\[(\d*)" #Pattern to get everything in measobjecttoaddmodlist
        pattern2 = "measobjecttoaddmodlist"
        #neglen = len("reportconfig")
    elif info_type == 2:
        pattern = r"reportconfigtoaddmodlist\[(\d*)" #Pattern for reportConfigToAddModList
        pattern2 = "reportconfigtoaddmodlist"
        #neglen = len("measidto")
    elif info_type == 3:
        pattern = r"measidtoaddmodlist\[(\d*)" #Pattern for measIdtoAddModList
        pattern2 = "measidtoaddmodlist"
        #neglen = 0
        
    reportconfigtoaddmodlist = []
    mtoaddid = -1
    current_key_vals = []
    test_key_vals = {}

    for i in clean_res(info_string).split(SPLIT_PATTERN):
        if i.find(pattern2) > -1:
            if len(current_key_vals) > 0:
                #reportconfigtoaddmodlist.append({mtoaddid: current_key_vals})
                reportconfigtoaddmodlist.append({mtoaddid: test_key_vals})

            current_key_vals = [] #reset the keys inside a measurement
            test_key_vals = {}

            mtoaddid = re.findall(pattern, i)[0] if re.findall(pattern, i) is not None else -1
            #print(re.findall(r"measidtoaddmodlist\[(\d*)", i)[0])
            #print(mtoaddid)

        else:
            keyval = i.split(":")
            #print( { keyval[0]: keyval[1] })
            if len(keyval) <= 1:
                current_key_vals.append( keyval )
                test_key_vals.update( {keyval[0]: ""} )
            else:
                current_key_vals.append({ keyval[0]: " ".join(keyval[1:]) })
                test_key_vals.update( { keyval[0]: " ".join(keyval[1:]) } )
                
    if len(current_key_vals) > 0:
        #reportconfigtoaddmodlist.append({mtoaddid: current_key_vals})
        reportconfigtoaddmodlist.append({mtoaddid: test_key_vals})

    
    return reportconfigtoaddmodlist
    
    
def get_rrc_info_main(info_type, info_string):
    '''
        combines the function to return a type of specific information dictionary.
        info_type = 1 : MeasObjectId (like earfcn and PCI...)
        info_type = 2 : ReportConfiguration (like event a5/a3 ....)
        info_type = 3 : MeasInfo (combines the above 2 to indicate type of measurement)
    '''
    ret_str, span = get_information(info_type, info_string)
    
    if ret_str is not None:
        return decode_rpt_type(info_type, ret_str), span
    return None, (-1, -1)


def find_reportconfig(report_cfg, cfg_number):
    '''
        Tries to find the configurations in the report_cfg dictionary related to a specific id
    
    '''
    assert type(cfg_number) == str, "Please use the string type as report config as per the code"
    
    for i in report_cfg:
        for j, k in i.items():
            assert 'reportconfigid' in k, "New edge case detected. Please check code and actual values. k = {}".format(k)
            if k['reportconfigid'] == cfg_number:
                return k
    return None

def find_measobject(measobj_cfg, cfg_number):
    '''
        Tries to find the configurations in the measobj_cfg dictionary related to a specific id
    
    '''
    assert type(cfg_number) == str, "Please use the string type as report config as per the code"
    
    for i in measobj_cfg:
        for j, k in i.items():
            assert 'measobjectid' in k, "New edge case detected. Please check code and actual values. k = {}".format(k)
            if k['measobjectid'] == cfg_number:
                return k
    return None



def process_main(current_text):
    print("Processing. ")


    measobjectids, span1 = get_rrc_info_main(1, current_text)
    reportconfigs, span2 = get_rrc_info_main(2, current_text)
    measids, span3 = get_rrc_info_main(3, current_text)
    
    print(span1, span2, span3)
    max_span = max(span1[1], span2[1], span3[1])
    min_span = min(span1[1], span2[1], span3[1])
    if min_span == -1:
        return None, ""
    
    ret = []
    for i in measids:
        row = {}
        for j, k in i.items():
            assert 'measid' in k, "New edge case detected. Please check code and actual values. k = {}".format(k)
            assert 'measobjectid' in k, "New edge case detected. Please check code and actual values. k = {}".format(k)
            assert 'reportconfigid', "New edge case detected. Please check code and actual values. k = {}".format(k)
            #print(k)
            
            k['measid'] = j #AAM - Rewrite the ids to save all
            
            
            rc = find_reportconfig( reportconfigs, k['reportconfigid'] )
            mo = find_measobject( measobjectids, k['measobjectid'] )

            row = k
            row.update(rc)
            row.update(mo)

            ret.append(row)
    print("Appended information together. Total length of measurement Ids is {}".format(len(ret)))



    ###########################################################################################
    # Display the results now.
    ###########################################################################################

    main_keys = ["measid",
                 "eventid",
                 "reportconfig",
                 "measobject",
                 
                 "ssbfrequency",
                 
                 "a1-threshold",
                 "a2-threshold",
                 "a3-offset", 
                 "a4-threshold",
                 'a5-threshold1',
                 'a5-threshold2',
                 "a6-offset-r10",
                 
                 
                 "b1-threshold",
                 "b2-threshold1",
                 "b2-threshold2",



                 "triggertype",
                 "purpose",


                 "reportonleave",
                 "a6-reportonleave-r10",
                 
                 "hysteresis", 
                 "timetotrigger", 
                 
                 "triggerquantity",
                 "reportquantity",
                 
                 "maxreportcells",
                 
                 "reportinterval",
                 "reportamount",


                 "carrierfreq",
                 "offsetfreq",
                 "physcellid",
                 "cellindividualoffset"
                ]


    if len(ret) <= 0:
        return None, ""
    row = []
    for i in ret:
        row.append({x:y for x,y in i.items() if x in main_keys})

    df = pd.DataFrame( row ).fillna("")
    all_columns = [x for x in main_keys if x in df.columns]
    all_columns.extend([x for x in df.columns if x not in main_keys])
    df = df[all_columns]
    
    df = df.T
    df.columns = df.loc['measid']
    df = df[df.index != 'measid']
    return df, current_text[max_span: ]

#############################################################################################################################
#############################################################################################################################

st.title('(Non-Dummy Proof) DT Measurement Config Tabular Display')

sample_text = st.text_area(label = 'Paste DT Measurement Config Text Here', value=c)
submit_button = st.button(label = "Process")
if submit_button:
    max_span = 0
    
    df = -1
    t = []
    while df is not None:
        df, sample_text= process_main(sample_text)
        if df is None:
            break
        else:
            st.table( df.copy() )

    
    #st.dataframe(mydf)

#############################################################################################################################
#############################################################################################################################