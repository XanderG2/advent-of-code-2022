from math import floor, ceil

example = """mjpsHcssDzLTzMsz
tFhbtClRVtbhRCGBFntNTrLhqrwqWMDMTWTqMq
LltbngLGRSBgSgGRCJdSdQHvdfmQccmjSQ
lBslsZDDWdGdGpSMts
grQhDvqLQHDNGJJtbRMQQJ
HChCTnnLCgCrTZPPFzzVPcVD
ShrzjhNGrNqrhWnHHfVHbhnHbbhH
RBsvcBcDCdsRTsvgCgcPFRQpVQGQJPVFbnJfbJ
DvsTsdlCBsGLrjzmlqqz
WJJqZTgCnBLGCZBJCJnTLggTDDSDDMNdDSdbdSSsWDFfMsFf
PVjqpVHmPpvmcjhrRprFmQQffbfNbQMMsSMQNQ
cwcpRvrVlVgwtBwZqBzZ
qfJJmpqpmhsggvvpVPZCrhdFLFzZFDdLLh
CtCTBctGcGLSzZddGZSW
RlNjBCnjttBHHMMcQHCsRfsbfwgggmmJvmgfpm
ZmcgBBZhZMsnqnCPjpHPjLHp
dGbNwNtlTMTzGfNvTvdwNGVLPpQHPjLQPCpCjPqjLbpLPR
dvDTdfvNBhDZMBDZ
cvvRvbqcllbBVlvVVbVVlbVDjRjDjdMsHPZPGdDPGPHrDP
FwtpfwJtWwNtTTNnwFCtjDJsQdQPPPPMrjrPJHjH
CwFpnppgntShgbsscbms
cWMFMQpFNcvNDdBDgdsT
MPrrfrCHBBsDZCBJ
LmLjMLjjLWpVcRVR
ZrRZqlZMqTWrMDqwvnvVtnsvddvVnlVf
pQNhhLNNGmLjhhcfvndDpffdfdVf
QGjCLCQGmNgPBQDFFgTMJWWwMRTrTZWWBWTr
WrZWZPHHWZHprZVmVvqddBttBBhGhtvh
gzDlMTJDMfqhBGllhl
jJLqMMDDbbqjLpPHcsHLWZspPr
bsSVRVGsrDstrrSjcQjcjlPwzjQl
gHBggFNTTvTgfqgCFzljWwLWQQQnrwQWnf
NvJHgpgHvqBhNBJhHTvpBCJCZmtdpDsGsZdZMZRbVbbMdrZs
MPPtPwPnRnMPPnwrtNSGgLSCGGGNSLtSgD
hBhWFjfCsTbbbWqFFWBBqBhsWZVGSVglZHLSVDlNWDNHHGgV
zsCfTsTCMdmRPwzQ
JVQVvvszzvTsVsVJjctppcCtjtPRcTlP
MdFgqSddMqMDbtDlNjRDSR
qFZWZqwHlZfZvzvZfLZn
vpqwQSsHSHDQzDpgzwZlRLRZRRZTnTrrvGhh
JBcdmbmFMPgPbgfrZRZnRFFnrnLRln
JNdBNgbdJmPMWSSDzwVDtwSWWW
BDMcDDppHCStpWcHBDNtzPJjqGlllPMJzPGjwjlq
CZdZLmgCdqbPzjblZj
vndLfnghRQmVrhdvgBHpSCDWHBBCVHNppD
WrhrJJGSWzpTWwts
VlLPmqgmRNZRGwsvttjgcwsT
PDZmlbdVqLmPlddVNRDmmmbbSFHrCFQCnFBFJHSJGrDQCBrr
hvPdpvhHvHvPrNfVhDfjggFfRV
zlGwJGslsSDRfjsg
MJMWjMJzwqWGzJwMqJBTCmHndPPdCBvmdCpmHn
PVWFpQhJhFJpGbRCvRHGCp
jgslDjftsqhNglTgllgTqMnlHwCcvwZwRccSRCbGSGbCMHRw
TgjhNNnjlTfjTdDqTfhjnmzmWPzWrLdrQBPJFWJWBB
qPPRMPlfSzSSSPPnnLnqMlpQQtrrtmWpbFtQrdzrtrWt
BBvCcwsVThsBgswDBCFQHQpdmQvtrFpWFvWp
gCghTJgVCgDGVMlRGMqZnSWqlM
RWbHvrbHBsbWBHJWvJwMtmdZwdtmdvwMZQff
DRVjcqhRchhGGllhCgdGQQzfttzGQGwQfg
cDRljchpqTcjDFTFVcPcPCWBHpNnJNNSnbWbHHrSpWHr
dtHrRrBHrCRhddftjgBrRhgjsbbbMpbSWSTjWcsDTWDbcW
GQPFVQVQnJlqVMDcMzpDfzpDVD
qZZJFLlLnvFFGPGLPqnJvwQldfgHrBRBmBhgNBRHghNhhwRg
rLbrZhPgqZhMdVFSFTSGCqFG
zsszfRzjtHtzvRTSDdFFCtdDdtND
fcwllfmwzRHlfmmzFvQQLrgLMLBZhJQZPrZhJLhW
sllrCfpQQJpMHLgzwDwpNqzzVDpV
RZPFZPGcSMFtGPRGMwNDVwdRgzvNwgqNvg
hBmbMcBmcThmcGtSFTZfQCJjrHLJfsjhWJssJl
DqGCbGfCRhfZCVbbqDJJGJBgRNpNdpBNNgNBBNwHnRgt
rcWSsSSPSQtwBwHD
MLscLMzvvTvcTLzvWWFDPTTrGqmFGGqCZJGbblbVbVZZVmFJ
FprpsLQTrstQHNmVSVml
JMggWPggWcRbwgJPCGMcGcfmzHlMNSjfzVNhHfVtzSMz
cwnPnBwgnGRgRCgRbWJLpFsLtFBLFrDLFZZDrL
lVgjLLLMgFMDCwCFqCRbngsvnGSvnSGndbsfgf
WZJcTWcNTmJZphmTJJNQHcdvfdbvnRRGbGthdrbttfSv
ZPQTJTpTNPJNQTmJRBZJNBHjwMVwPCMwVlVzjwwzqqjVjL
hznNhNQNQFDWVFmDQm
SMqZBMMbBvDbHPzzdVPH
zzzTBTMLNTgpnTTh
NLCdmsdCVLGHCHdQzzmznnFwRjFMDMwpTBjDRpnpTBMJ
PrcfcrglcfWbSqgrlqvShrwpJpDBFJHpBWjTDTRTRTTB
crSgSHtPttfdLGmtzzZNNV
BTlTVqCBqtTcBqVhWlsJjDvsnLsvlvpJPj
gMgggGZbSMzNRRRLmZZnQZQPPDvnsnDvJwwQ
dMRRmMgbNfRgmfSdGFgNgTBtrhrhqfWtLCCWLTWWHc
zcfVrPwnwrPmrvnjdFdBbHFFdd
CCqpSSQQpQZLDCSHPpBFvFBjTHRvRR
DMLGthLZMLtQGhGNMPqGSDflzfwcVmzJzsfgNVrswcrr
hSgvMTQvChSqPvhTrRLlVHJgfgRJlHHHJH
jmzsZzZzwmmLGGtwtVJWNNDRDtVcfVRl
GnBBLbzzzFszBFpzvSdrQQCTCQbhMvSQ
VHpTMrZMMbDbbpTZmQmTnmzhTqjqlWWQ
GGvgNsvNCNvvGvlqqdzWZmlsmZqZ
wNNNgccNGJSNBSRNBNvNcvJHLDDZMFRMppMLrfHDLbrrHF
spssbPMLpPllspGNsNWMrnwddnfcqrnwwwwMwM
VmQBFCjzzjmfnwbrngcVrd
FQbSFjBvvzsWvWGlvWNl
JLFSwfwRLLfGhnQJBQshvn
pZgNcpCWpWtcvhjGGjtVvszD
CccMcPcgTTCWmcZcWMcmTNZPmHdrqSHFRRrqwrSrRqwrHmsH
BPMhflJRhqnPNGjNRNRjgSRm
VdVsDswTVZbCwCZBrcDCczTwtjtNNjmjmgpmjpQggpGVSgQm
sTbWrsTBbrTPPnqlJnPPhW
nvrgjMWBvQWPvQnsZfGcZcRFdGFtdtZB
bHVDwmqNNDhHNzqpphLNHVLpSJcdZtfffRZdDgRFGSddcRZt
HNLNqNqLNbhqVVbClngjnQWPTWgsCgvT
tfstpcScscBTFTpFnsWSmgdzJlgmgBmPPzJmvdPm
jnrqrLHRwGrwhdPvvPvhjJmP
qqCLRCGrZZqCHRVtVWQptFWppnbcWb
wCDJZJgDwHpdqHhdGHBhhH
WSPmJMlmbSmztQlQsvPhnhGGdBddBqdGddTbVB
WzWQftWMSWtmvmmSWtMQPgggpZwLwZjggJFgrpFCfj
MvQBJMBQhjQFNFnjnj
dtlZmRtLmjSTSLLtTtNVwWzDRzDVwwWFwnNn
dmmLCqTdcLqtLGqjBhpfHqBGpv
PBPRhjTPPlLRBvlvfwffqJGfpG
rHtMtrszFtSgbFrrggrFgMnwWGzmQqWvGWzGQpJGfNqqNz
FggcbSMntVgMdRCwZcjChLCT
lCqqBlCwlnDqPZTZZBLNdjJLwttNWjjdzJzc
fVfMbvbvmbVsmSsmMVWNtzzcjgLWgjztMMtg
VVmFhFRSfbQsvVQmvSfhSsmzHlCZqrrBrDBrHZPRTZnnzB
CRrDWmzRRQMmDqrrBgBQmtHljhHwtwlwplcBjHGwwB
PWfPSWnvsNZSZdfjHjZtGHjchllltl
WVsnbSPTbNdbmqTQmmrmLzTq
cGtMBGSJDgtgMBsBMgMvWWSHWjpjzHTWTPpqWzqW
mNVQNsdVsdhLmCpTWWjmCjTT
NQQwrfbQrNQNbrrdLwfQsZdgFbBBFBgggRGRDMRFFMRDgM
lFnqgqWQvHWqgvlVglvqjPjcLdfLfBPLnrbLNLcN
hmTmthppsRtpTRRTZMpSbLdNjNcJLcrcBNbJBZZc
smmpRsTtpSSsRGhppmmhdCMGWwqFQgWGWWDgWwVFHQqHgg
mWFjmcdcFWcSSQjzrpvrwRGvTwQGGG
HRJfgMZVhtRlHJHBVJTGvGppbpbvvGTvTtrv
glsgVMVqffdnPRDcqLnL
MtvLJdmLLTvSSCtSzLSTcDhRjRftQjjssshfQNjPtf
nlggrFWzRsfFjVQN
WgwwBgbgZBHGBnccTzMCLTZJmLLL
sRtHTBBHZtDTtZhdPzWdGcdVFdJmGcnm
wpwMLWCgvfNvwvwbbCrwgfzPncrJPSFVGPnrcJSVznmV
bLpvwQwMwpjWMgfvgZTsDsBttqHRjTqHlH
mpmGpCpmlpmwfmCQVppCVfQSSjvSqgWvvvDgNwWDgnnDnW
RBLsHRJBRrHJWFDWSNqFWj
zZBLdsdcZrsBjGfpGVpTTPGlVc
NBbTzgwSNmrFWpVrzrFM
LnZQtQlZVnMrFBBG
CCdtddBtPdNqcvHSCCcg
ZFbZPHbZPTQVVlsGNF
qtvDWvgRftqGNccCNVThDs
fRwGBBjBppdMdBMZ
GffflsZsPZVfjsssNfZsJNNZVcMDSqMWFcwFMMpcTMTTFSTS
LhrCmvzcRbbhtmRdTCMDwWMpDWqqqMpW
dvRQmBBvLzBRRvRhhcdbhdRgjHQNllJsfsNlZZljZGGNQN
wjbMPsbfLzVCTMVbjLplmpshhSpHShhJhtsm
ZrcqZTDTGDqFdJtGmdGSpl
QNNrWvQRqRNWnTQRvqjPbjfWbCBCMbMLBwMV
wRPRsppFfWJRlPRPFlpJfwSMzzZTBwBtZTTCMCMtdz
vGLGrjcfrLVGjfnGTMCMtNNnCTnMtCBd
VrjqhjhLVcrGVRqJmqQspmfFWm
LRfdnmwMwdSBmfvJNrrgLhCNgqqJWs
llctPPVTcPStgJgshCsrCs
DpTlFpFVRFZRFFSv
sPgRgsmdcqmgSvvFRRRRdqdFfTWZhhdZrZbbWfTpwDfbWTbw
jLCCHtLljJzjlplfZSlwTfprZZ
tBHVjQHzHQJBtSVmvRsvvFRqnGgv
spppVDbVcbgVSFgFZZbGZgbJMRBTvHTvJJHGtHRwtMGvHT
LldflzQLLQmQWQQfnwMWwHJtTtwRBcBt
CPjfhCmNmNfFVchpchFVhp
bZQJgQmQmTgnLBRtNPNnml
ccszcqldGzhszrVsqdlHVNwLpppwHPHRtBBppDNRLt
VSzVhVdcfrrhcqGrVhrssQQlMbJvFjMgbFSQggCvCv
hHWVWhhlZDZVWNTgczWLjbtcTFFj
JJnPnCdBCBnnRCjSsjStBgsbFttb
MRpgCpGqdPRppJwpnRqRfZZhmvhHDrhllDHhhZGZ
SPcgLDcLLnWFWCNVCRPT
fhZQtsbtmbmfZTVTVRWfNvTCTT
jhbbmzRsQzpLDcgLHLjg
GSFRHrCCGRJDJtrgWdrL
stcVQshQZBsBmjMsZhmMQQWDDvNWdncNWvzLgdDnzdDN
sVwMBQBhVVjtQZVPlSfPCfwRpSCpRl
bBHHJMJvBvWMJWqqccNNPhMCrclChQCC
RPppPgfpwgmcQgrhmm
tfwTwpFPGGwZSRtpVjJHbHLvSvLSqVLL
jlJfZGjljJPBqJGnfGVMqGfrFWWddvDmFRDcmdFDdDvbDM
hTCTsgsgwhTbvRdcFmsddpFd
wbQNHTQLgCwSThhCgwnZnJfqnqJBlNlBnnVl
CLlfbjjbLlbbDGbLzfCGhdtdWBthdBWsHvWHBnntWs
rmJRJFqrDwVFTwFmSJvtvMtdJMMHBdBBndWt
ZVrVVZpgTpZFSqmZqRNlNNfQQbpGjDQbbpPl
mVCrhGHGmZhrNlDwbWnLWWvGLWWwnd
PNsqgzspsgNFJNFfzqpWSWdwSvSPnvdWbSbvjd
NzgJzqMcgscQqJcpJRzBmlrBRBDDlHZBBBHtHZ
NJmNJDwcMmJNMbJJDNDqcGcsWRWHQzRPQjZLRGZWLQsjZQ
dgSnTBgdpddtgShSTZjLRhRLHqWPPhPRPQ
VgdTpBntlvBVrlfcbqJcMrfmcqmb
wvqwvPwNJgFmLdvDJFDmDLvJlQZpMzSpBVflpdSSMlQnfldS
WjCcRZCWRjjRtsZhRRhpSVBVnzplBfWnfBfSQz
CbRbcsjHZrhbTRtsGbCrgNgDDPFFqvvJvJFDFw
GlsCrbCChShqgqlbSCcVbqgVhBwjBDFBhBhdDWvwBFFvWvDv
THmHMmtMnLfHRnzRZnfLBDWWsWzWFNsvWjjvjvFF
mpHRtmZffHTTMpmLMLLnJtJCgScScsPlblcpCrPbblCPlq
vscDLrcvrsLNStdTfBCvgJTqGBdd
bwLbzRhbbdTfbgCB
pplQzLwmPZVMStcDjFtQrS
RMjCrhFJhRVRVCCFFsvmnvqrmbvqmqSmbrvm
tzfpBgTHzttGzZpBfHGDBZHbccnGqbmvdNlGnSnlcvSwbn
pDWTHDTzgTfWZpVVsWSPjRFSMsFs
fmrfmrwVfjmrzjqCsqqvjsvvpG
hFDVtFStVtJnPPtJNHbtQWGbQsCvCsQgpWGggdQC
NBSDSNHStHNHnhStHNNrcflrmTzBlwmzrlMVVw
SjtZZSdNcDldPQqndl
BbgzgWgTmTBfwrbnDjQDwVPwDlnsVq
zBBrCTTMBWLMWmfMfbbmrMtjNZLFJRRZSSvFFtStvGGJ
CTCGLGCFRRSMGnZnLCTfdffhpbNbDfpdZBvhdv
rJlqclVPHJWVrgPPQqjqgJlhBhDBBQdvbhwvNfhswfNpvb
tltrcrHjlVWVCDzSGCCzLCGt
sbHHsbCCHbLSVfJbbfSLNJBzvzMMPrhPPNztZlZNZhdt
GTWjplTgDnGmQGpQnQhZrvvBMPztPzvrzvjZ
mQgGWllcFcTFmgwcDppDQGTCqfsSLqsfSbqJqLSSFsbRfF
jslsFjLLLLvFwWtQFTFDJQWp
dGzdrNmRWqVBGcTbwpRDRnbJDRhT
qzqzrrPNNrmfLPsjglHjgW
QjCHcPfcgQSgPPcffQSmmmLmrJJpNpBMrJMtFrBBBMFrrpNS
VGVZfDbbVVZWGvDbFrlBZNJBNlNMwwtM
sbvfhqTGTRnhTVGvzgHmgQLQmPqzmPLm
sLwnMHnbnLMjGpZsjGGtpc
ggvJrNNTQgQrNvgqBqZCCjClWjGtWjCpGJFW
TVdrqvVrTNTzBqQQzTRMfHbMwMbZMdMbHwRD
bcfJQQJHsQPCpdpWdPbb
RHjHDwZtrZmRDDtwtjRBVFdWVrrrBClldVphCF
zDgwgNzjmDnMnzMMHncG
vMHRvMhvHWRBRDHhRBwWvRBqLqbGwqnqnnNTbNqdNbbVVr
pslgcZszJltrsZcZgNnnqbSSTSSndbNbzS
cZcgsZgZZgPgmcpfJtfttWBQvmFWjDQDhBmFjDHvFr
bVbBvdTTVLbCgCznLJsJcwHPczfz
NFcDphSDrFjGtZNZjplZGZFnzPHPrzHHzJMnnwfPsPsRJs
cGtGljFmWdvqmVCV
qSNbTvcvTGTvGcgtBNvcbdrdjrnjRnjRVHdDqHrRHj
ZZZZPLWPzPDCCsCRnRdwVFnjdwPVFP
ChlCLLZftfcBvfDv
cRtfctVgmRclmBFGbbMBDDFPtD
svQZhHSHssjTvjpQjSSBBMJMJGDBpPbMzzpGzP
ZsvsCTWhCHhSwwjrwbndldlRnfRNmb
PQdTgdGpRcTccCfj
hHFLHlHBhBlmlDFzHrhhfZNZbfNZcVWNVVZRDjCC
LFLLMHJHSBhBFGGnMMvsGtGGtj
fwmVnVCDVqpNQqqb
ddBcZZWdvGWzBzsWvLvddlNHcHQPbQqqJQNNQHPHQT
WgGvsMMzvgbntDhCmt
JjwhFMmwjJwmCgTgSCSFlPLg
WWbsbVtftBZWtnWtncbQvctTGLpLgCpzPPPlllpzlgPPTQ
TBvnfBffWsfVtTvbZBTNjwjqddhMNqwRMMhdRMrq
SllrbtTSQrSQrbrvvMvzFDsBsssWpWdWbGpGBWNWNW
hhCfmmmjmPLCfmnPLfqPgqqNNBpjZBZQDNQdpWNpdBBsBp
RhLfPhQLQfCRnHfqTHHrFJMrttTwTtzt
BFrFBJMMJnnsNJBFCdLCnmvzbPdCmPnc
LDLVHQRfDvdHdcCmcv
llQDwqSVLwZLZSgsGZMNMgTjTMTr
mrwdbqRhdCNGgZBHbH
jVTPMjvjpvMfTfQfPlpHHZNnNBHgZDGsGMnCsZ
TLlfQpffQvvzhtNqztRFtzcm
DDfvJZZPDHVPSPcSvcgcWCsWQcTTdhQTTh
dMwpbdjRtrFhhTsTFQWqhC
bGRdNpbzlvLfDfZlLZ
bdPQdcpdbpjFqpQcQwqqhhNRhJvWRfrrWBsJrfwN
mMtlZfmtnLZtSnGDlmGWRRhrWLhJsBRvgRWghh
DnMGCtmCzfGMbjdQbVzpqcFH
jwnGggRBvvpBZCljCsCWrhhrsh
FVMcFLqLMqcJfVtDqMJcHMHWCSblzzrWsdhSLlSzbrGCLz
HQVFPDtDQDFFNTZpPgNnGgNn
HNBHNqlqHJQBRNvdmZvmPdZZlpnT
bDbbhDgSfzVVfnvPmfHmTZZd
jgzbwrhVsDgsDWLwJqqBMqcqHL
tzNtJzsJVBHzbjbglCHc
nfmnGnmPhntCgHvtvmCj
MStTwrMTWrTdBZSNLZJNVQ
NVjmwmVGGwGFHstwFHMhTh
psRSzzscZscZpgQQzqQtBBHTTlThHHtTTh
rCprbpZccggcrRzbbRRbscvVVWWvNfvVWnGDCWVNddmd
rphfGDgtPtllrPlFlGrhGjnmnTnjcBsncBBVpTTBmc
SqqZMJCLwgCwJgQRqqgZQNwdBBsBBHVBdTHNsnVNBTccnc
MJqZZMbqgzRCSJZwPtFfGzWhrrfGttWl
cSZqqcwbqVzqCbqVqVZPsvvDCDrffngvphggndhdGh
tTNTMWJNQJHMNGSSprfdGnfdth
WNRHWWMJSRWzswbczsVPRs
HCgcSMhSMBGMdvGf
RNQqbDQqFdRFdmTZfGtPZvtGlQffll
mNpdNrRDbTNrmbpzmpWmbpWcswhcHcjhscSHjSgVHwHn
MwgcFgwMMcscCbMFsMFCgMgPPLWPvptvBvPvtvvWmBBzwG
nhQQjTJRVDdQJrPpmnGGBmvtGvLz
HdJQdJHjrJQDBQjhQVQJhdJcqlFHcSqsNbCbCqCHFqCFgC
JvTnvWtdJLbhJHbMwwHjcGHCwHwQGQ
mqtmsllmfqVFwMwMrrPjmQrC
lfztRZSlRDRVzfdpWnSvWhNdbnpp
rSvrgggzHTNzrHtnptpmlDngZjWj
MdMhqMhsfMSRcGqRsQQRctjjdDnjtjClCjjpZnDlnt
BBMRsQRfRcscGqBfRRsBssPBLLzNLFPwvVFFPTLbbLwHHTvS
pCmCfdPFzmsFsDhFFDsttptpRtJjLnlJRtttHt
ZQwgWZgqJhTTRtgV
GNqWNvcqqQQrMMWcQzDDsSzBDBSssSmhhr"""

def partone():
    global example
    lines = example.splitlines()
    current = []
    outliars = []
    outliarsForThisRound = []
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabetList = list(alphabet)
    index = 0
    total = 0
    for x in lines:
        List = list(x)
        lenList = len(List)
        comp1 = List[:floor(lenList/2)]
        comp2 = List[ceil(lenList/2):]
        for i in comp2:
            if i in comp1:
                if i not in outliarsForThisRound:
                    outliars += [i]
                    outliarsForThisRound += [i]
        outliarsForThisRound = []
    for x in outliars:
        index = alphabetList.index(x) + 1
        total += index
    print(f"part one: {total}")
                   

def parttwo():
    global example
    individual = example.splitlines()
    group = ""
    groupOfThree = []
    num = 0
    one = []
    two = []
    three = []
    numTwo = 0
    outliarsThisRound = set()
    outliars = []
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabetList = list(alphabet)
    index = 0
    total = 0
    for x in range(int(len(individual)/3)):
        group = "\n".join(individual[num:num+3])
        groupOfThree += [group]
        num += 3
    for x in groupOfThree:
        current = x.split("\n")
        one = []
        two = []
        three = []
        numTwo = 0
        outliarsThisRound = set()
        for y in current:
            numTwo += 1
            if numTwo == 1:
                one = list(y)
            elif numTwo == 2:
                two = list(y)
            elif numTwo == 3:
                three = list(y)
                for i in three:
                    if i in one and i in two:
                        if i not in outliarsThisRound:
                            outliars += [i]
                            outliarsThisRound.add(i)
        outliarsThisRound = set()
    for x in outliars:
        index = alphabetList.index(x) + 1
        total += index
    print(f"part two: {total}")
            
                    
                

partone()
parttwo()



























    
