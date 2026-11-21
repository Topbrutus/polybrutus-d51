#!/usr/bin/env python3
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
c=json.loads((R/'results/certificate_d51.json').read_text(encoding='utf8'))
m=json.loads((R/'publication/zenodo_metadata_blueprint.json').read_text(encoding='utf8'))
assert c['status']=='PASS' and c['dimension']==m['scientific_dimension']==51
assert c['vertices']==m['norm_one_vertices']==56
assert c['pairs']==m['exact_labelled_squared_pairs']==1540
assert c['affine_rank']==c['centered_gram_rank']==51
assert c['eigenvalue_28_multiplicity']==m['model_eigenvalue_28_multiplicity']==45
assert c['eigenvalue_55_over_2_multiplicity']==m['model_eigenvalue_55_over_2_multiplicity']==4
assert c['parent_tag_commit']=='e94150cdafe611ef3522fc77de76bf931a64b749'
assert c['parent_doi']==m['scientific_parent_doi']=='10.5281/zenodo.24429826'
assert m['related_identifiers']==[{'identifier':'10.5281/zenodo.24429826','relation':'isDerivedFrom','resource_type':'publication-preprint','scheme':'doi'}]
assert len(m['keywords'])==9
assert 'affine Euclidean dimension fifty-one' in m['keywords']
assert 'forty-fivefold ideal eigenvalue' in m['keywords']
assert len(m['references'])==2
assert '10.5281/zenodo.24429826' in m['references'][0]
assert '10.5281/zenodo.24407952' in m['references'][1]
assert not any(x in str(m['keywords']) for x in ('fifty-two','forty-sixfold','forty-fourfold','dimension fifty '))
note=(R/'publication/POLYBRUTUS_51D_NOTE.md').read_text(encoding='utf8')
assert all(v in note for v in ('## References','10.5281/zenodo.24429826','10.5281/zenodo.24407952'))
print('D51_ZENODO_CURRENT_KEYWORDS_PARENT_RELATION_AND_TWO_REFERENCES_GATE_PASS')
