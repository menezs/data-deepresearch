[referencia=d9c08b4d6cd4e69f score=0.068]
```

---

[referencia=d9c08b4d6cd4e69f score=0.068]
```

---

[referencia=d9c08b4d6cd4e69f score=0.068]
```

---

[referencia=d9c08b4d6cd4e69f score=0.068]
```

---

[referencia=d9c08b4d6cd4e69f score=0.068]
```

---

[referencia=d9c08b4d6cd4e69f score=0.068]
```

---

[referencia=d9c08b4d6cd4e69f score=0.068]
```

---

[referencia=d9c08b4d6cd4e69f score=0.035]
## 19.3 BPE merges in a didactic corpus

**File:** `03_bpe_didatico.py`. **Function.** Executes eight BPE steps over the corpus low (5), lower (2), newest (6), and widest (3), using `</w>` as the end-of-word marker. At each step it prints the merged pair, its frequency, the three most frequent pairs, and the resulting vocabulary. Ties are resolved by order of occurrence.

**Supports.** The merge table in Section 3.

```
import re, collections
vocab={"l o w </w>":5,"l o w e r </w>":2,"n e w e s t </w>":6,"w i d e s t </w>":3}
def stats(v):
    p=collections.Counter()
    for w,f in v.items():
        s=w.split()
        for a,b in zip(s,s[1:]): p[(a,b)]+=f
    return p
def merge(pair,v):
    out={}
    bg=re.escape(" ".join(pair)); pat=re.compile(r'(?<!\S)'+bg+r'(?!\S)')
    for w,f in v.items(): out[pat.sub("".join(pair),w)]=f
    return out
for i in range(8):
    p=stats(vocab); best=max(p,key=lambda k:(p[k],))
    top=p.most_common(3)
    print(i+1,best,p[best],top[:3]); vocab=merge(best,vocab); print("  ",vocab)
```

---

[referencia=d9c08b4d6cd4e69f score=0.035]
## 19.3 BPE merges in a didactic corpus

**File:** `03_bpe_didatico.py`. **Function.** Executes eight BPE steps over the corpus low (5), lower (2), newest (6), and widest (3), using `</w>` as the end-of-word marker. At each step it prints the merged pair, its frequency, the three most frequent pairs, and the resulting vocabulary. Ties are resolved by order of occurrence.

**Supports.** The merge table in Section 3.

```
import re, collections
vocab={"l o w </w>":5,"l o w e r </w>":2,"n e w e s t </w>":6,"w i d e s t </w>":3}
def stats(v):
    p=collections.Counter()
    for w,f in v.items():
        s=w.split()
        for a,b in zip(s,s[1:]): p[(a,b)]+=f
    return p
def merge(pair,v):
    out={}
    bg=re.escape(" ".join(pair)); pat=re.compile(r'(?<!\S)'+bg+r'(?!\S)')
    for w,f in v.items(): out[pat.sub("".join(pair),w)]=f
    return out
for i in range(8):
    p=stats(vocab); best=max(p,key=lambda k:(p[k],))
    top=p.most_common(3)
    print(i+1,best,p[best],top[:3]); vocab=merge(best,vocab); print("  ",vocab)
```

---

[referencia=d9c08b4d6cd4e69f score=0.032]
# disambiguation
feat=["dinheiro","assento","pessoas","madeira"]
emb={"O":[0,0,0,0],"banco":[.7,.7,0,0],"estava":[0,0,.1,0],"lotado":[0,0,1,0],
"de":[0,0,0,0],"clientes":[.8,0,.7,0],"da":[0,0,0,0],"praça":[0,.8,0,.2],"madeira":[0,.3,0,1],"velho":[0,.2,0,.5],"gerente":[.9,0,.3,0],"fila":[.5,0,.9,0]}
def ctx(words, scale=2.0):
    Em=np.array([emb[w] for w in words],float)
    # Q=K=E*scale + vetor de sentinela p/ evitar nulos
    Q=K=Em*scale
    S=Q@K.T/np.sqrt(4)
    bi=words.index("banco")
    S[bi,:]+=0  # sem alteração
    A=sm(S)
    Z=A@Em
    return A[bi],Z[bi]
protoF=np.array([1,0,.5,0]);protoP=np.array([0,1,0,.5])
cos=lambda a,b:a@b/np.linalg.norm(a)/np.linalg.norm(b)
for name,w in [("fin",["O","banco","estava","lotado","de","clientes"]),("praca",["O","banco","da","praça","estava","velho","madeira"]),("isolado",["banco"])]:
    a,z=ctx(w); print(name,w,a,z,"cosFin",cos(z,protoF),"cosPraca",cos(z,protoP))
```

---

[referencia=d9c08b4d6cd4e69f score=0.032]
# disambiguation
feat=["dinheiro","assento","pessoas","madeira"]
emb={"O":[0,0,0,0],"banco":[.7,.7,0,0],"estava":[0,0,.1,0],"lotado":[0,0,1,0],
"de":[0,0,0,0],"clientes":[.8,0,.7,0],"da":[0,0,0,0],"praça":[0,.8,0,.2],"madeira":[0,.3,0,1],"velho":[0,.2,0,.5],"gerente":[.9,0,.3,0],"fila":[.5,0,.9,0]}
def ctx(words, scale=2.0):
    Em=np.array([emb[w] for w in words],float)
    # Q=K=E*scale + vetor de sentinela p/ evitar nulos
    Q=K=Em*scale
    S=Q@K.T/np.sqrt(4)
    bi=words.index("banco")
    S[bi,:]+=0  # sem alteração
    A=sm(S)
    Z=A@Em
    return A[bi],Z[bi]
protoF=np.array([1,0,.5,0]);protoP=np.array([0,1,0,.5])
cos=lambda a,b:a@b/np.linalg.norm(a)/np.linalg.norm(b)
for name,w in [("fin",["O","banco","estava","lotado","de","clientes"]),("praca",["O","banco","da","praça","estava","velho","madeira"]),("isolado",["banco"])]:
    a,z=ctx(w); print(name,w,a,z,"cosFin",cos(z,protoF),"cosPraca",cos(z,protoP))
```

---

[referencia=d9c08b4d6cd4e69f score=0.015]
## 19. Source code (Python)

**Purpose of this section.** It makes the article’s numbers, figures, and auxiliary files reproducible. The numerical examples have didactic value only if readers can rerun them and obtain the same results.

The programs below are reproduced as executed. Run 19.1 first, then 19.2, which reads the file written by 19.1; programs 19.3 and 19.4 can follow; 19.5 uses the files from 19.1 and 19.2. Dependencies are Python 3, NumPy, Matplotlib, and requests. The calculations in 19.1–19.4 were rerun from scratch before publication and reproduced the values cited in Sections 4–7, 11, and 12. Under this edition’s editorial policy, routines used exclusively to write PNG or PDF metadata are not included in the document.

Not reproduced are: (a) the parameter counts in Sections 6 and 8, which are direct arithmetic performed without a script; (b) editing tools used to insert text and links; and © conversion commands using Pandoc and XeLaTeX.

---

[referencia=d9c08b4d6cd4e69f score=0.013]
## 19.6 Extraction of bibliography links

**File:** `07_gerar_csv_links.py`. **Function.** Reads Section 18 from the Markdown file and generates `links_bibliografia.csv` with author, year, expected title, URL, and audit status for each entry.

**Supports.** Input for Program 19.7.

```
import re,csv
s=open("abrindo-a-caixa-preta-da-inferencia-em-llms.md",encoding="utf-8").read()
# delimits Section 18 before the code appendix
ref=s.split("## 18. Bibliography / References")[1].split("## 19.")[0]
items=[l[2:] for l in ref.splitlines() if l.startswith("- ")]
rows=[]
for it in items:
    cite=it.split("(")[0].strip().rstrip(",;. ")
    yr=re.search(r"\((\d{4}[ab]?)\)\.\s+(.*)",it)
    rest=yr.group(2)
    m=re.match(r"(.*?[?!])\s|(.*?)\.\s",rest)
    titulo=(m.group(1) or m.group(2)) if m else rest[:80]
    urls=re.findall(r"<(https?://[^>]+)>",it)
    aud="link auditado" in it
    rows.append([len(rows)+1,cite.split(";")[0]+(" et al." if ";" in cite else ""),yr.group(1),titulo,urls[0],"auditado (busca)" if aud else "nao auditado"])
with open("links_bibliografia.csv","w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f); w.writerow(["n","autor","ano","titulo_esperado","url","status_auditoria_20261020"]); w.writerows(rows)
```

---

[referencia=d9c08b4d6cd4e69f score=0.009]
Sc=Ss.copy(); Sc[mask]=-np.inf; Ac=sm(Sc); print("Acausal\n",Ac)
# project back with Wo (2->4)
Wo=np.array([[1,0,0.5,0],[0,1,0,0.5]],float)
O=Z@Wo; print("O\n",O)
R=X+O; print("R\n",R)
def ln(x,eps=1e-5): m=x.mean(-1,keepdims=True); v=x.var(-1,keepdims=True); return (x-m)/np.sqrt(v+eps)
Y=ln(R); print("LN\n",Y)
# rms
rms=R/np.sqrt((R**2).mean(-1,keepdims=True)+1e-5); print("RMS\n",rms)
# FFN d_ff=8 ReLU
rng=np.random.default_rng(0)
W1=rng.normal(0,0.5,(4,8)); b1=np.zeros(8); W2=rng.normal(0,0.5,(8,4)); b2=np.zeros(4)
H=np.maximum(0,Y@W1+b1); F=H@W2+b2
print("W1\n",W1,"\nW2\n",W2)
print("H\n",H,"\nF\n",F)
Y2=ln(Y+F); print("Y2\n",Y2)
# output: vocab
vocab=["lotado","vazio","cheio","aberto","verde"]
Wout=rng.normal(0,0.8,(4,5))
lg=Y2[2]@Wout  # posição de "estava" prevê próxima palavra
print("Wout\n",Wout,"\nlogits",lg)
p=sm(lg); print("p",p, p.sum())
for T in [0.5,1.0,2.0]:
    print(T, sm(lg/T))
tgt=0; print("CE",-np.log(p[tgt]))
# top-p
order=np.argsort(-p); cs=np.cumsum(p[order]); print([vocab[i] for i in order],cs)

---

[referencia=d9c08b4d6cd4e69f score=0.009]
Sc=Ss.copy(); Sc[mask]=-np.inf; Ac=sm(Sc); print("Acausal\n",Ac)
# project back with Wo (2->4)
Wo=np.array([[1,0,0.5,0],[0,1,0,0.5]],float)
O=Z@Wo; print("O\n",O)
R=X+O; print("R\n",R)
def ln(x,eps=1e-5): m=x.mean(-1,keepdims=True); v=x.var(-1,keepdims=True); return (x-m)/np.sqrt(v+eps)
Y=ln(R); print("LN\n",Y)
# rms
rms=R/np.sqrt((R**2).mean(-1,keepdims=True)+1e-5); print("RMS\n",rms)
# FFN d_ff=8 ReLU
rng=np.random.default_rng(0)
W1=rng.normal(0,0.5,(4,8)); b1=np.zeros(8); W2=rng.normal(0,0.5,(8,4)); b2=np.zeros(4)
H=np.maximum(0,Y@W1+b1); F=H@W2+b2
print("W1\n",W1,"\nW2\n",W2)
print("H\n",H,"\nF\n",F)
Y2=ln(Y+F); print("Y2\n",Y2)
# output: vocab
vocab=["lotado","vazio","cheio","aberto","verde"]
Wout=rng.normal(0,0.8,(4,5))
lg=Y2[2]@Wout  # posição de "estava" prevê próxima palavra
print("Wout\n",Wout,"\nlogits",lg)
p=sm(lg); print("p",p, p.sum())
for T in [0.5,1.0,2.0]:
    print(T, sm(lg/T))
tgt=0; print("CE",-np.log(p[tgt]))
# top-p
order=np.argsort(-p); cs=np.cumsum(p[order]); print([vocab[i] for i in order],cs)

---

[referencia=d9c08b4d6cd4e69f score=0.007]
import numpy as np
np.set_printoptions(precision=3, suppress=True)
d=np.load("toy.npz"); 
def sm(z): z=z-z.max(-1,keepdims=True); e=np.exp(z); return e/e.sum(-1,keepdims=True)
def ln(x,eps=1e-5): m=x.mean(-1,keepdims=True); v=x.var(-1,keepdims=True); return (x-m)/np.sqrt(v+eps)
X,V,Ac=d["X"],d["V"],d["Ac"]
Wo=np.array([[1,0,0.5,0],[0,1,0,0.5]],float)
Zc=Ac@V; Oc=Zc@Wo; Rc=X+Oc; Yc=ln(Rc)
print("Zc\n",Zc,"\nOc\n",Oc,"\nRc\n",Rc,"\nYc\n",Yc)
rng=np.random.default_rng(0)
W1=rng.normal(0,0.5,(4,8)); W2=rng.normal(0,0.5,(8,4))
H=np.maximum(0,Yc@W1); F=H@W2; Y2=ln(Yc+F)
print("H\n",H,"\nF\n",F,"\nY2\n",Y2)
Wout=rng.normal(0,0.8,(4,5)); vocab=["lotado","vazio","cheio","aberto","verde"]
lg=Y2[2]@Wout; p=sm(lg)
print("Wout\n",Wout,"\nlg",lg,"\np",p)
for T in [0.5,1,2]: print(T,sm(lg/T))
print("CE lotado",-np.log(p[0]),"CE cheio",-np.log(p[2]))
o=np.argsort(-p); print([vocab[i] for i in o], np.cumsum(p[o]))
np.savez("toy2.npz",Zc=Zc,Oc=Oc,Rc=Rc,Yc=Yc,H=H,F=F,Y2=Y2,Wout=Wout,lg=lg,p=p,W1=W1,W2=W2)
# disambiguation
feat=["dinheiro","assento","pessoas","madeira"]

---

[referencia=d9c08b4d6cd4e69f score=0.007]
import numpy as np
np.set_printoptions(precision=3, suppress=True)
d=np.load("toy.npz"); 
def sm(z): z=z-z.max(-1,keepdims=True); e=np.exp(z); return e/e.sum(-1,keepdims=True)
def ln(x,eps=1e-5): m=x.mean(-1,keepdims=True); v=x.var(-1,keepdims=True); return (x-m)/np.sqrt(v+eps)
X,V,Ac=d["X"],d["V"],d["Ac"]
Wo=np.array([[1,0,0.5,0],[0,1,0,0.5]],float)
Zc=Ac@V; Oc=Zc@Wo; Rc=X+Oc; Yc=ln(Rc)
print("Zc\n",Zc,"\nOc\n",Oc,"\nRc\n",Rc,"\nYc\n",Yc)
rng=np.random.default_rng(0)
W1=rng.normal(0,0.5,(4,8)); W2=rng.normal(0,0.5,(8,4))
H=np.maximum(0,Yc@W1); F=H@W2; Y2=ln(Yc+F)
print("H\n",H,"\nF\n",F,"\nY2\n",Y2)
Wout=rng.normal(0,0.8,(4,5)); vocab=["lotado","vazio","cheio","aberto","verde"]
lg=Y2[2]@Wout; p=sm(lg)
print("Wout\n",Wout,"\nlg",lg,"\np",p)
for T in [0.5,1,2]: print(T,sm(lg/T))
print("CE lotado",-np.log(p[0]),"CE cheio",-np.log(p[2]))
o=np.argsort(-p); print([vocab[i] for i in o], np.cumsum(p[o]))
np.savez("toy2.npz",Zc=Zc,Oc=Oc,Rc=Rc,Yc=Yc,H=H,F=F,Y2=Y2,Wout=Wout,lg=lg,p=p,W1=W1,W2=W2)
# disambiguation
feat=["dinheiro","assento","pessoas","madeira"]

---

[referencia=d9c08b4d6cd4e69f score=0.007]
tgt=0; print("CE",-np.log(p[tgt]))
# top-p
order=np.argsort(-p); cs=np.cumsum(p[order]); print([vocab[i] for i in order],cs)
np.savez("toy.npz",E=E,P=P,X=X,Q=Q,K=K,V=V,S=S,Ss=Ss,A=A,Ac=Ac,Z=Z,O=O,R=R,Y=Y,H=H,F=F,Y2=Y2,lg=lg,p=p)
```

---

[referencia=d9c08b4d6cd4e69f score=0.007]
tgt=0; print("CE",-np.log(p[tgt]))
# top-p
order=np.argsort(-p); cs=np.cumsum(p[order]); print([vocab[i] for i in order],cs)
np.savez("toy.npz",E=E,P=P,X=X,Q=Q,K=K,V=V,S=S,Ss=Ss,A=A,Ac=Ac,Z=Z,O=O,R=R,Y=Y,H=H,F=F,Y2=Y2,lg=lg,p=p)
```

---

[referencia=d9c08b4d6cd4e69f score=0.006]
## 13. Emergent properties and scaling laws

**Purpose of this section.** It explains how a behavior such as disambiguation can exist without being explicitly programmed, linking the result of Section 12 to the training process in Section 10. It frames the debate on emergence without claiming more than the literature supports.

**Concept.** An **emergent property** is a characteristic of the system as a whole that is not programmed into any single component and arises from large-scale interaction among components (Anderson, 1972). Transformer code contains only matrix multiplications, additions, normalizations, and softmax; the training objective is only to predict the next token. Nothing explicitly names word senses, syntax, or reasoning, yet representations of this kind appear in the learned weights (Sections 9 and 12). A common analogy is an ant colony: no individual ant “knows” how to build a bridge, yet the colony builds one.

**Capabilities that emerge with scale.** Wei et al. (2022a) define an emergent capability as one that is absent in smaller models and present in larger models such that its appearance cannot be predicted by simple extrapolation from the smaller-model curves. Examples discussed in the literature include few-shot prompting in large models (Brown et al., 2020) and chain-of-thought reasoning (Wei et al., 2022b).

**Scaling laws.** While average prediction loss improves smoothly and predictably with parameters, data, and compute (Kaplan et al., 2020; Hoffmann et al., 2022), performance on specific tasks may appear to change abruptly. Ganguli et al. (2022) discuss this combination of predictability in loss and surprise in capabilities.

**Debate: genuine emergence or a metric effect?** Schaeffer et al. (2023) argue that some observed jumps result from discontinuous metrics, such as exact match, and that continuous metrics applied to the same models reveal gradual progress. The debate remains open, and the literature advises caution when claiming that a capability “suddenly appears.”