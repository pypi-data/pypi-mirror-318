import{b as c,ee as q,d as E,ea as N,N as R,O as _,e as p,X as D,o as B,Y as P,w as g,u,a as V,bT as x,aG as O,dj as h,c_ as L,cO as S,a0 as $}from"./index.fd9b9ab8.js";import{G as z}from"./PhDownloadSimple.vue.ae25310a.js";import{e as A}from"./toggleHighContrast.106416e2.js";import"./gateway.304ae457.js";import{a as M}from"./project.df2d8960.js";import"./tables.7da5ab67.js";import"./popupNotifcation.29b8d844.js";import"./record.b518ae74.js";import"./string.b5cc208c.js";(function(){try{var t=typeof window<"u"?window:typeof global<"u"?global:typeof self<"u"?self:{},a=new Error().stack;a&&(t._sentryDebugIds=t._sentryDebugIds||{},t._sentryDebugIds[a]="bb70c845-de54-4035-8e07-345df21ee48c",t._sentryDebugIdIdentifier="sentry-dbid-bb70c845-de54-4035-8e07-345df21ee48c")}catch{}})();var T={icon:{tag:"svg",attrs:{viewBox:"0 0 1024 1024",focusable:"false"},children:[{tag:"path",attrs:{d:"M715.8 493.5L335 165.1c-14.2-12.2-35-1.2-35 18.5v656.8c0 19.7 20.8 30.7 35 18.5l380.8-328.4c10.9-9.4 10.9-27.6 0-37z"}}]},name:"caret-right",theme:"outlined"};const F=T;function C(t){for(var a=1;a<arguments.length;a++){var e=arguments[a]!=null?Object(arguments[a]):{},r=Object.keys(e);typeof Object.getOwnPropertySymbols=="function"&&(r=r.concat(Object.getOwnPropertySymbols(e).filter(function(d){return Object.getOwnPropertyDescriptor(e,d).enumerable}))),r.forEach(function(d){G(t,d,e[d])})}return t}function G(t,a,e){return a in t?Object.defineProperty(t,a,{value:e,enumerable:!0,configurable:!0,writable:!0}):t[a]=e,t}var w=function(a,e){var r=C({},a,e.attrs);return c(q,C({},r,{icon:F}),null)};w.displayName="CaretRightOutlined";w.inheritAttrs=!1;const H=w,J=t=>{let a=t.columns.join(",")+`
`;t.rows.forEach(r=>{a+=r.join(","),a+=`
`});const e=document.createElement("a");e.href="data:text/csv;charset=utf-8,"+encodeURIComponent(a),e.target="_blank",e.download=`${t.fileName}.csv`,e.click()};function U(t){const a={};for(const e in t)if(t.hasOwnProperty(e)){if(typeof t[e]=="object"&&t[e]!==null){a[e]=JSON.stringify(t[e]);continue}a[e]=String(t[e])}return a}const X={class:"container"},Y=E({__name:"Sql",setup(t){const e=N().params.projectId,r=new R(_.array(_.object({projectId:_.string(),lastQuery:_.string()})),"lastQueries"),d=p(null),f=p(""),v=p([]),y=p([]),I=p([]),b=p(!1),Q=async()=>{b.value=!0;const s=await M.executeQuery(e,f.value,[]);b.value=!1;const o=r.get();if(!o)r.set([{projectId:e,lastQuery:f.value}]);else{const n=o.findIndex(l=>l.projectId===e);n===-1?o.push({projectId:e,lastQuery:f.value}):o[n].lastQuery=f.value,r.set(o)}if(!s)return;const{returns:m,errors:i}=s;I.value=i;for(const n of i)S.error({message:"SQL Execution Failed",description:n});i.length||S.success({message:"SQL Execution Succeeded"}),y.value=m.fields.map(n=>({title:n.name,key:n.name,dataIndex:n.name})),v.value=m.result.map((n,l)=>U({key:`${l+1}`,...n}))},j=()=>{const s=y.value.map(l=>l.dataIndex),o=y.value.map(l=>l.title),m=v.value.map(l=>s.map(k=>l[k])),n=`data-${new Date().toISOString()}`;J({fileName:n,columns:o,rows:m})};return D(()=>{var m;const s=A.create(d.value,{language:"sql",value:f.value,fontFamily:"monospace",lineNumbers:"on",minimap:{enabled:!1},scrollbar:{vertical:"hidden",horizontal:"visible"},fontSize:14,scrollBeyondLastLine:!1,lineHeight:20});s.onDidChangeModelContent(()=>{f.value=s.getValue()});const o=r.get();if(o){const i=(m=o.find(n=>n.projectId===e))==null?void 0:m.lastQuery;i&&(f.value=i,s.setValue(i))}}),(s,o)=>(B(),P("div",X,[c(u(h),{gap:"large",class:"sql-container",align:"center"},{default:g(()=>[V("div",{ref_key:"sqlEditor",ref:d,class:"sql-editor"},null,512),c(u(x),{type:"primary",loading:b.value,onClick:Q},{icon:g(()=>[c(u(H))]),default:g(()=>[O(" Run ")]),_:1},8,["loading"])]),_:1}),c(u(h),{justify:"end",style:{margin:"30px 0 10px 0"}},{default:g(()=>[c(u(x),{disabled:!v.value.length,onClick:j},{default:g(()=>[c(u(h),{align:"center",gap:"small"},{default:g(()=>[O(" Export to CSV "),c(u(z))]),_:1})]),_:1},8,["disabled"])]),_:1}),c(u(L),{style:{width:"100%"},scroll:{x:100},"data-source":v.value,columns:y.value},null,8,["data-source","columns"])]))}});const se=$(Y,[["__scopeId","data-v-6f35762f"]]);export{se as default};
//# sourceMappingURL=Sql.b5d9ff87.js.map
