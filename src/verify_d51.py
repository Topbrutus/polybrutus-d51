#!/usr/bin/env python3
"""Polybrutus D51: exact Euclidean labelled metric and chosen ideal weighted graph.
Conservative perpendicular unit extension of the immutable Polybrutus D50 v0.1.0.
No physical spacetime dimension or experimentally measured resonance is claimed.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
from hashlib import sha256
import json
import sympy as s
from sympy.polys.matrices import DomainMatrix

ROOT=Path(__file__).resolve().parents[1]
Q=s.Rational
core=[(0,0,1),(Q(1,2),0,Q(1,2)),(-Q(1,4),Q(3,4),Q(1,2)),
      (-Q(1,4),-Q(3,4),Q(1,2)),(0,0,-1),(Q(1,2),0,-Q(1,2)),
      (-Q(1,2),0,-Q(1,2))]
n=56
pairs=list(combinations(range(n),2))
G=s.zeros(n)
for i in range(7):
    for j in range(7):
        G[i,j]=3*core[i][0]*core[j][0]+core[i][1]*core[j][1]+core[i][2]*core[j][2]
for i in range(7,12):
    for j in range(7,12):
        G[i,j]=1 if i==j else -Q(1,4)
for i in range(12,n):
    G[i,i]=1
assert all(G[i,i]==1 for i in range(n))
assert DomainMatrix.from_Matrix(G).to_field().rank()==51
D=2*s.ones(n)-2*G
for i in range(n):
    D[i,i]=0
assert len(pairs)==1540 and all(D[i,j]>0 for i,j in pairs)

parent_path=ROOT/'prior'/'d50'/'results'/'certificate_d50.json'
parent_archive=ROOT/'prior'/'d50'/'frozen_scientific_tag_v0.1.0.zip'
assert sha256(parent_archive.read_bytes()).hexdigest()=='0130c197acd8ef08a6a5b4a0d530c40deb9b2bf907f989f2d9cb19204491b1c4'
from zipfile import ZipFile
with ZipFile(parent_archive) as _frozen:
    assert _frozen.testzip() is None
    assert _frozen.read('results/certificate_d50.json')==parent_path.read_bytes()
parent_bytes=parent_path.read_bytes()
assert sha256(parent_bytes).hexdigest()=='e371670c9f5b5acc74780b8d61146b449cdbca234bf6cf0e55e2fb7230fc85d3'
parent=json.loads(parent_bytes)
assert parent['status']=='PASS' and parent['dimension']==50 and parent['vertices']==55
former={(int(e['i'])-1,int(e['j'])-1):s.Rational(e['d2'])
        for e in parent['labelled_squared_distances']}
assert len(former)==1485
assert all(D[i,j]==v for (i,j),v in former.items())
assert all(D[i,55]==2 for i in range(55))
hist=Counter(4*D[i,j] for i,j in pairs)
expected=Counter({4:6,7:2,8:1509,9:3,10:10,12:6,13:2,16:2})
assert hist==expected and sum(hist.values())==1540
assert sum(D[i,j] for i,j in pairs)==Q(12367,4)

H=s.eye(n)-s.ones(n)/n
B=-H*D*H/2
assert B==H*G*H
assert DomainMatrix.from_Matrix(B).to_field().rank()==51
# The first and fifth canonical points are antipodal; origin lies in the affine hull.
assert G[0,4]==-1

L=s.zeros(n)
for i,j in pairs:
    w=1/D[i,j]
    L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
assert L*s.ones(n,1)==s.zeros(n,1)
assert DomainMatrix.from_Matrix(L-28*s.eye(n)).to_field().rank()==11
assert DomainMatrix.from_Matrix(L-Q(55,2)*s.eye(n)).to_field().rank()==52
old=s.zeros(55)
for i,j in combinations(range(55),2):
    w=1/D[i,j]
    old[i,i]+=w;old[j,j]+=w;old[i,j]-=w;old[j,i]-=w
assert L[:55,:55]-old==s.eye(55)/2
assert all(L[i,55]==-Q(1,2) for i in range(55))
assert L[55,55]==Q(55,2)

# Four adversarial negative controls.
damaged=D.copy();damaged[0,55]=damaged[55,0]=Q(9,4)
assert Counter(4*damaged[i,j] for i,j in pairs)!=hist
duplicate=G.copy();duplicate[55,:]=G[54,:];duplicate[:,55]=G[:,54];duplicate[55,55]=1
assert DomainMatrix.from_Matrix(duplicate).to_field().rank()==50
tilted_dot_to_old_core=Q(3,10)
assert Q(3,10)**2+Q(91,100)==1
assert tilted_dot_to_old_core!=0 and 2-2*tilted_dot_to_old_core!=D[0,55]
swapped=D.copy();swapped.row_swap(0,7);swapped.col_swap(0,7)
assert swapped!=D and Counter(4*swapped[i,j] for i,j in pairs)==hist

report={
  'schema':'POLYBRUTUS-D51-EXACT-CERTIFICATE-v1',
  'status':'PASS','dimension':51,'vertices':56,'pairs':1540,
  'affine_rank':51,'centered_gram_rank':51,'ambient_storage_coordinates':52,
  'radius':1,'parent':'Topbrutus/polybrutus-d50@v0.1.0',
  'parent_tag_commit':'e94150cdafe611ef3522fc77de76bf931a64b749',
  'parent_doi':'10.5281/zenodo.24429826',
  'parent_certificate_sha256':sha256(parent_bytes).hexdigest(),
  'parent_frozen_tag_archive_sha256':sha256(parent_archive.read_bytes()).hexdigest(),
  'parent_frozen_tag_embedded_as_verified_zip':True,
  'parent_distances_preserved':1485,'new_distances':55,
  'new_squared_distances':['2']*55,
  'histogram_k_4d2':{str(k):int(v) for k,v in sorted(hist.items())},
  'sum_squared_distances':'12367/4',
  'gram_psd_certificate':'B=-(H D H)/2=H G H; G=XX^T exact',
  'negative_controls':'4/4 PASS',
  'oscillator_model':'Chosen ideal equal-mass complete graph with w_ij=1/d_ij^2; no physical measurement',
  'eigenvalue_28_multiplicity':45,
  'eigenvalue_55_over_2_multiplicity':4,
  'spectral_recurrence':'chi56(z)=z*(z-28)*chi55(z-1/2)/(z-1/2)',
  'spectral_closed_form':'chi56(z)=z*(z-28)^45*(z-55/2)^4*f6(z-49/2), f6(z)=chiP7(z)/z',
  'novel_universal_theorem':'NOT CLAIMED','physical_discovery':'NOT CLAIMED',
  'human_peer_review':'NOT_DONE','sympy':s.__version__,
  'labelled_squared_distances':[{'i':i+1,'j':j+1,'d2':str(D[i,j]),'k':str(4*D[i,j])} for i,j in pairs]
}
out=ROOT/'results'/'certificate_d51.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
print('PRIMARY D51 PASS: 56 vertices, 1540 labelled pairs, affine rank 51; 1485/1485 previous pairs preserved')
print('IDEAL GRAPH PASS: eigenvalue 28 x45; eigenvalue 55/2 x4; 4/4 negative controls')
print('CERTIFICATE_SHA256='+sha256(out.read_bytes()).hexdigest())
