import{r as O}from"./router.d43eb07e.js";import{_ as P}from"./DocsButton.vue_vue_type_script_setup_true_lang.365ce5ce.js";import{i as E}from"./url.9ba27ecc.js";import{G as L}from"./PhDotsThreeVertical.vue.c27507a1.js";import{d as M,E as j,e as N,o as s,c as r,w as l,u as n,cO as G,b as y,Y as A,eb as T,cB as Q,bL as W,cG as Y,aB as Z,aS as B,cW as q,aG as d,e9 as f,S as g,cA as H,cN as J,f as X,r as K,dj as D,df as ee,$ as V,dd as F,bT as te,c_ as ae,Z as le,de as x,d7 as U,bR as ne,bz as se,bx as oe,a as ue,ec as re,cQ as ie,by as pe,a0 as ce}from"./index.fd9b9ab8.js";import{A as R,a as ye}from"./index.d03e071b.js";import{B as de}from"./Badge.7af0d9ba.js";import{A as z}from"./index.1b35746e.js";(function(){try{var _=typeof window<"u"?window:typeof global<"u"?global:typeof self<"u"?self:{},m=new Error().stack;m&&(_._sentryDebugIds=_._sentryDebugIds||{},_._sentryDebugIds[m]="e808f867-6362-407a-a34a-0a6ed8527441",_._sentryDebugIdIdentifier="sentry-dbid-e808f867-6362-407a-a34a-0a6ed8527441")}catch{}})();const fe=M({__name:"CreationModal",props:{entityName:{},fields:{},create:{type:Function}},setup(_,{expose:m}){const b=_,I=`Create ${b.entityName}`,c=j({inputValue:{}}),C=N(!1),k=()=>C.value=!0,w=()=>{C.value=!1,c.inputValue={}},S=async()=>{try{await b.create(c.inputValue),w()}catch(p){p instanceof Error&&G.error({message:"Failed to create",description:p.message})}},t=(p,o)=>{const e=p.target.value,a=b.fields.find(i=>i.key===o);a!=null&&a.format?c.inputValue[o]=a.format(e):c.inputValue[o]=e},v=(p,o)=>{const e=p.target.value,a=b.fields.find(i=>i.key===o);a!=null&&a.blur?c.inputValue[o]=a.blur(e):c.inputValue[o]=e};return m({open:k,close:w}),(p,o)=>(s(),r(n(J),{open:C.value,title:I,onCancel:w,onOk:S},{default:l(()=>[y(n(H),{layout:"vertical"},{default:l(()=>[(s(!0),A(B,null,T(p.fields,e=>{var a;return s(),r(n(Q),{key:e.key,label:e.label,help:(a=e.hint)==null?void 0:a.call(e,c.inputValue[e.key])},{default:l(()=>{var i,h,$;return[!e.type||e.type==="text"||e.type==="password"?(s(),r(n(W),{key:0,value:c.inputValue[e.key],"onUpdate:value":u=>c.inputValue[e.key]=u,placeholder:(i=e.placeholder)!=null?i:"",type:(h=e.type)!=null?h:"text",onInput:u=>t(u,e.key),onBlur:u=>v(u,e.key)},null,8,["value","onUpdate:value","placeholder","type","onInput","onBlur"])):e.type==="multiline-text"?(s(),r(n(Y),{key:1,value:c.inputValue[e.key],"onUpdate:value":u=>c.inputValue[e.key]=u,placeholder:($=e.placeholder)!=null?$:"",onInput:u=>t(u,e.key),onBlur:u=>v(u,e.key)},null,8,["value","onUpdate:value","placeholder","onInput","onBlur"])):e.type==="select"?(s(),r(n(Z),{key:2,value:c.inputValue[e.key],"onUpdate:value":u=>c.inputValue[e.key]=u,mode:e.mode},{default:l(()=>[(s(!0),A(B,null,T(e.options,u=>(s(),r(n(q),{key:typeof u=="string"?u:u.value,value:typeof u=="string"?u:u.value},{default:l(()=>[d(f(typeof u=="string"?u:u.label),1)]),_:2},1032,["value"]))),128))]),_:2},1032,["value","onUpdate:value","mode"])):g("",!0)]}),_:2},1032,["label","help"])}),128))]),_:1})]),_:1},8,["open"]))}}),me={class:"action-item"},ve=M({__name:"CrudView",props:{table:{},loading:{type:Boolean},title:{},emptyTitle:{},entityName:{},description:{},create:{type:Function},createButtonText:{},docsPath:{},live:{type:Boolean},fields:{}},setup(_){const m=_,b=N(null),I=(t,v)=>{var o;const p=(o=m.table.rows[0])==null?void 0:o.cells[v].type;if(!(p==="actions"||p==="slot"))return(e,a)=>c(e,a,v)},c=(t,v,p)=>{const o=t.cells[p],e=v.cells[p];return o.type==="text"&&e.type==="text"||o.type==="tag"&&e.type==="tag"?o.text.localeCompare(e.text):o.type==="tags"&&e.type==="tags"?o.tags[0].text.localeCompare(e.tags[0].text):o.type==="secret"&&e.type==="secret"||o.type==="link"&&e.type==="link"?o.text.localeCompare(e.text):(o.type==="actions"&&e.type==="actions",0)},C=async()=>{var t;m.fields?(t=b.value)==null||t.open():m.create&&await m.create({})},k=N(!1);async function w(t,v){if(!k.value){k.value=!0;try{"onClick"in t?await t.onClick({key:v.key}):"link"in t&&(typeof t.link=="string"&&E(t.link)?open(t.link,"_blank"):O.push(t.link))}finally{k.value=!1}}}const S=X(()=>({"--columnCount":`${m.table.columns.length}`}));return(t,v)=>{const p=K("RouterLink");return s(),A(B,null,[y(n(z),{direction:"vertical",class:"crud-view"},{default:l(()=>{var o;return[y(n(D),{align:"center",justify:"space-between"},{default:l(()=>[t.title?(s(),r(n(ee),{key:0},{default:l(()=>[d(f(t.title),1)]),_:1})):g("",!0),V(t.$slots,"more",{},void 0,!0)]),_:3}),t.description?(s(),r(n(F),{key:0},{default:l(()=>[d(f(t.description)+" ",1),V(t.$slots,"description",{},void 0,!0),t.docsPath?(s(),r(P,{key:0,path:t.docsPath},null,8,["path"])):g("",!0)]),_:3})):g("",!0),y(n(D),{gap:"middle"},{default:l(()=>[t.createButtonText?(s(),r(n(te),{key:0,type:"primary",onClick:C},{default:l(()=>[d(f(t.createButtonText),1)]),_:1})):g("",!0),V(t.$slots,"secondary",{},void 0,!0)]),_:3}),V(t.$slots,"extra",{},void 0,!0),y(n(ae),{"filter-dropdown":!0,size:"small",style:le(S.value),"data-source":t.table.rows,loading:k.value||t.loading&&!t.live,height:400,columns:(o=t.table.columns)==null?void 0:o.map((e,a)=>{var i;return{...e,key:a,filtered:!0,align:(i=e.align)!=null?i:"center",sorter:I(e,a)}})},{emptyText:l(()=>[d(f(t.emptyTitle),1)]),headerCell:l(e=>[d(f(e.title),1)]),bodyCell:l(({column:{key:e},record:a})=>[a.cells[e].type==="slot"?V(t.$slots,a.cells[e].key,{key:0,payload:a.cells[e].payload},void 0,!0):(s(),r(n(ie),{key:1,open:a.cells[e].hover?void 0:!1},{content:l(()=>[y(n(F),{style:{width:"300px",overflow:"auto","font-family":"monospace"},copyable:"",content:a.cells[e].hover},null,8,["content"])]),default:l(()=>[a.cells[e].type==="text"?(s(),r(n(x),{key:0,secondary:a.cells[e].secondary,code:a.cells[e].code},{default:l(()=>[y(n(de),{dot:a.cells[e].contentType==="warning",color:"#faad14"},{default:l(()=>[d(f(a.cells[e].text),1)]),_:2},1032,["dot"])]),_:2},1032,["secondary","code"])):a.cells[e].type==="secret"?(s(),r(n(x),{key:1,copyable:{text:a.cells[e].text}},{default:l(()=>[d(" ******** ")]),_:2},1032,["copyable"])):a.cells[e].type==="tag"?(s(),r(n(U),{key:2,color:a.cells[e].tagColor},{default:l(()=>[d(f(a.cells[e].text),1)]),_:2},1032,["color"])):a.cells[e].type==="tags"?(s(),r(n(z),{key:3},{default:l(()=>[(s(!0),A(B,null,T(a.cells[e].tags,(i,h)=>(s(),r(n(U),{key:h,color:i.color},{default:l(()=>[d(f(i.text),1)]),_:2},1032,["color"]))),128))]),_:2},1024)):a.cells[e].type==="link"?(s(),r(p,{key:4,to:a.cells[e].to},{default:l(()=>[d(f(a.cells[e].text),1)]),_:2},1032,["to"])):a.cells[e].type==="actions"?(s(),r(n(ne),{key:5},{overlay:l(()=>[y(n(se),{disabled:k.value},{default:l(()=>[(s(!0),A(B,null,T(a.cells[e].actions.filter(i=>!i.hide),(i,h)=>(s(),r(n(oe),{key:h,danger:i.dangerous,onClick:$=>w(i,a)},{default:l(()=>[ue("div",me,[i.icon?(s(),r(re(i.icon),{key:0})):g("",!0),y(n(x),null,{default:l(()=>[d(f(i.label),1)]),_:2},1024)])]),_:2},1032,["danger","onClick"]))),128))]),_:2},1032,["disabled"])]),default:l(()=>[y(n(L),{style:{cursor:"pointer"},size:"25px"})]),_:2},1024)):g("",!0)]),_:2},1032,["open"]))]),footer:l(()=>[t.live?(s(),r(n(ye),{key:0,justify:"end",gutter:10},{default:l(()=>[y(n(R),null,{default:l(()=>[y(n(pe),{size:"small"})]),_:1}),y(n(R),null,{default:l(()=>[y(n(x),null,{default:l(()=>[d(" auto updating ")]),_:1})]),_:1})]),_:1})):g("",!0)]),_:3},8,["style","data-source","loading","columns"])]}),_:3}),t.fields&&t.create?(s(),r(fe,{key:0,ref_key:"modalRef",ref:b,fields:t.fields,"entity-name":t.entityName,create:t.create},null,8,["fields","entity-name","create"])):g("",!0)],64)}}});const Ae=ce(ve,[["__scopeId","data-v-e8e1b31a"]]);export{Ae as C};
//# sourceMappingURL=CrudView.9d4fe7c6.js.map
