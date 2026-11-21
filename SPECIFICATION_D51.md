# Polybrutus D51 - exact 56-point rational Euclidean squared-distance metric

**Only scientific parent:** Topbrutus/polybrutus-d50@v0.1.0, peeled tag commit \`e94150cdafe611ef3522fc77de76bf931a64b749\`, DOI 10.5281/zenodo.24429826. Authentic original full source ZIP SHA-256 \`0130c197acd8ef08a6a5b4a0d530c40deb9b2bf907f989f2d9cb19204491b1c4\` and original certificate SHA-256 \`e371670c9f5b5acc74780b8d61146b449cdbca234bf6cf0e55e2fb7230fc85d3\`.

## Conservative norm-one Euclidean extension

Place all 55 old unit vectors p_i in a new Euclidean coordinate space by q_i=(p_i,0). Add one new perpendicular unit vector q_56. Then each of the 1485 old labelled squared distances is unchanged and each of the 55 new distances equals 2R², giving C(56,2)=1540 exact unordered labelled pairs.

The Gram G has block-orthogonal rational structure: seven canonical unit points with rank 3, an independent centered five-unit-simplex of rank 4 (mutual dot product -1/4), and 44 mutually independent orthogonal unit axes. Thus G=XXᵀ is PSD with unit diagonal and rank 3+4+44=51.

Define D_ij=2-2G_ij, i!=j; D_ii=0. Let H=I-11ᵀ/56, B=-(HDH)/2=HGH. B is PSD exact rank 51, and inherited antipodal canonical pair ensures the origin is in the affine hull. Hence the metric's minimum affine Euclidean realization dimension is 51; 52 storage coordinates suffice.

Exact histogram k=4d²/R²: 4:6, 7:2, 8:1509, 9:3, 10:10, 12:6, 13:2, 16:2, totaling 1540 unordered pairs. Sum of squared distances at R=1: **12367/4**.

## Separately chosen ideal graph

With scalar unit masses and edge weights w_ij=1/d_ij², each added perpendicular unit vertex introduces 55 edges of weight 1/2. Laplacian L51=[[L50+I55/2,-1_55/2],[-1_55ᵀ/2,55/2]]. Exact characteristic recurrence:
chi56(z)=z(z-28)chi55(z-1/2)/(z-1/2).
With seven-point factor f6(z)=chiP7(z)/z, the closed form is:
chi56(z)=z(z-28)^45(z-55/2)^4*f6(z-49/2).

The ideal Laplacian has eigenvalue 28 multiplicity 45 and 55/2 multiplicity 4 by exact rational rank-nullity. No physical frequency or spacetime claim.

**Bibliography:** D50 DOI 10.5281/zenodo.24429826, historical D7 DOI 10.5281/zenodo.24407952.
