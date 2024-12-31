import{C as A}from"./CrudView.9d4fe7c6.js";import{d as _,e as k,ea as x,f as v,o as C,Y as P,b as l,u as i,w as d,aS as h,dd as D,aG as f,de as M,e9 as N,cN as j,e_ as K,ep as T}from"./index.fd9b9ab8.js";import{a as V}from"./asyncComputed.7e5cce79.js";import{A as c}from"./apiKey.b636dd30.js";import"./gateway.304ae457.js";import{M as B}from"./member.b060b075.js";import{a as E}from"./project.df2d8960.js";import"./tables.7da5ab67.js";import"./router.d43eb07e.js";import"./Badge.7af0d9ba.js";import"./DocsButton.vue_vue_type_script_setup_true_lang.365ce5ce.js";import"./BookOutlined.e64b5e9e.js";import"./url.9ba27ecc.js";import"./PhDotsThreeVertical.vue.c27507a1.js";import"./index.d03e071b.js";import"./index.1b35746e.js";import"./popupNotifcation.29b8d844.js";import"./record.b518ae74.js";import"./string.b5cc208c.js";(function(){try{var n=typeof window<"u"?window:typeof global<"u"?global:typeof self<"u"?self:{},a=new Error().stack;a&&(n._sentryDebugIds=n._sentryDebugIds||{},n._sentryDebugIds[a]="fed2c81c-7233-40f9-a0c8-a4cf928bfbee",n._sentryDebugIdIdentifier="sentry-dbid-fed2c81c-7233-40f9-a0c8-a4cf928bfbee")}catch{}})();const ae=_({__name:"ApiKeys",setup(n){const a=k(null),p=[{key:"name",label:"API key name"}],s=x().params.projectId,y=new B,{loading:g,result:I,refetch:u}=V(async()=>Promise.all([c.list(s),E.get(s).then(e=>y.list(e.organizationId))]).then(([e,t])=>e.map(o=>({apiKey:o,member:t.find(r=>r.authorId===o.ownerId)})))),b=async e=>{const t=await c.create({projectId:s,name:e.name});u(),a.value=t.value},w=v(()=>{var e,t;return{columns:[{title:"Name"},{title:"Creation date"},{title:"Owner"},{title:"",align:"right"}],rows:(t=(e=I.value)==null?void 0:e.map(({apiKey:o,member:r})=>{var m;return{key:o.id,cells:[{type:"text",text:o.name},{type:"text",text:K(o.createdAt)},{type:"text",text:(m=r==null?void 0:r.email)!=null?m:"Unknown"},{type:"actions",actions:[{label:"Delete",icon:T,dangerous:!0,onClick:async()=>{await c.delete(s,o.id),u()}}]}]}}))!=null?t:[]}});return(e,t)=>(C(),P(h,null,[l(A,{"entity-name":"API key","create-button-text":"Create API Key",loading:i(g),title:"API Keys",description:"API Keys are used to deploy your project from the local editor.","empty-title":"No API keys here yet",table:w.value,fields:p,create:b},null,8,["loading","table"]),l(i(j),{open:!!a.value,title:"Api key generated",onCancel:t[0]||(t[0]=o=>a.value=null)},{footer:d(()=>[]),default:d(()=>[l(i(D),null,{default:d(()=>[f("Your API key was successfully generated. Use this code to login on your local development environment or deploy using CI")]),_:1}),l(i(M),{code:"",copyable:""},{default:d(()=>[f(N(a.value),1)]),_:1})]),_:1},8,["open"])],64))}});export{ae as default};
//# sourceMappingURL=ApiKeys.9df255f2.js.map
