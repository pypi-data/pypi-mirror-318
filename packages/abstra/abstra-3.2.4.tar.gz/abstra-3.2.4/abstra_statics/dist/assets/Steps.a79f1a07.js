import{A as n}from"./index.5fd6e71f.js";import{d as a,f as o,o as r,Y as c,b as f,u as l,Z as d,S as p,a0 as u}from"./index.fd9b9ab8.js";(function(){try{var e=typeof window<"u"?window:typeof global<"u"?global:typeof self<"u"?self:{},t=new Error().stack;t&&(e._sentryDebugIds=e._sentryDebugIds||{},e._sentryDebugIds[t]="5f1b8cda-5181-43c7-81b9-88877f63a606",e._sentryDebugIdIdentifier="sentry-dbid-5f1b8cda-5181-43c7-81b9-88877f63a606")}catch{}})();const i=a({__name:"Steps",props:{stepsInfo:{type:Object,default:null}},setup(e){const t=e,s=o(()=>t.stepsInfo?Array(t.stepsInfo.total).fill(null).map(()=>({label:"",description:""})):[]);return(m,_)=>e.stepsInfo?(r(),c("nav",{key:0,class:"p-steps",style:d({maxWidth:Math.min(e.stepsInfo.total*3.5,100)+"%"})},[f(l(n),{current:e.stepsInfo.current-1,items:s.value,responsive:!1},null,8,["current","items"])],4)):p("",!0)}});const I=u(i,[["__scopeId","data-v-1ef844ba"]]);export{I as S};
//# sourceMappingURL=Steps.a79f1a07.js.map
