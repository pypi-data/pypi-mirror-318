import{N as Z}from"./Navbar.c8d55bb0.js";import{B as y}from"./BaseLayout.1da2d684.js";import{C as A}from"./ContentLayout.6fdbd531.js";import{a as w}from"./asyncComputed.b9262f9a.js";import{d as b,D as p,f as s,o as t,Y as i,$ as _,S as f,e8 as M,a as n,ea as z,r as k,c as v,w as c,b as g,u as C}from"./index.313443c9.js";import{H as B}from"./PhCube.vue.af3ee818.js";import{F as I}from"./PhUsersThree.vue.b8c7f51a.js";import"./gateway.062e0276.js";import{a as S}from"./organization.6bc2177e.js";import"./tables.dc4b2117.js";import{S as N,_ as x}from"./Sidebar.90e40e76.js";import"./PhChats.vue.9a814b27.js";import"./PhSignOut.vue.958a79eb.js";import"./router.f4178cff.js";import"./Badge.eac660dd.js";import"./index.1b040ba8.js";import"./Avatar.63c22857.js";import"./index.5504e3fa.js";import"./index.35791209.js";import"./BookOutlined.3803112a.js";import"./popupNotifcation.b9f169b0.js";import"./record.7a34fecb.js";import"./string.1aa5755a.js";import"./index.33c86bc6.js";import"./AbstraLogo.vue_vue_type_script_setup_true_lang.5f0d7dd4.js";import"./Logo.4dd4184b.js";import"./index.43ac97d8.js";(function(){try{var r=typeof window<"u"?window:typeof global<"u"?global:typeof self<"u"?self:{},e=new Error().stack;e&&(r._sentryDebugIds=r._sentryDebugIds||{},r._sentryDebugIds[e]="c8ca2dcc-01b5-4ae0-8693-2d9b93d05e31",r._sentryDebugIdIdentifier="sentry-dbid-c8ca2dcc-01b5-4ae0-8693-2d9b93d05e31")}catch{}})();const D=["width","height","fill","transform"],$={key:0},j=n("path",{d:"M224,44H32A20,20,0,0,0,12,64V192a20,20,0,0,0,20,20H224a20,20,0,0,0,20-20V64A20,20,0,0,0,224,44Zm-4,24V88H36V68ZM36,188V112H220v76Zm172-24a12,12,0,0,1-12,12H164a12,12,0,0,1,0-24h32A12,12,0,0,1,208,164Zm-68,0a12,12,0,0,1-12,12H116a12,12,0,0,1,0-24h12A12,12,0,0,1,140,164Z"},null,-1),E=[j],P={key:1},O=n("path",{d:"M232,96v96a8,8,0,0,1-8,8H32a8,8,0,0,1-8-8V96Z",opacity:"0.2"},null,-1),R=n("path",{d:"M224,48H32A16,16,0,0,0,16,64V192a16,16,0,0,0,16,16H224a16,16,0,0,0,16-16V64A16,16,0,0,0,224,48Zm0,16V88H32V64Zm0,128H32V104H224v88Zm-16-24a8,8,0,0,1-8,8H168a8,8,0,0,1,0-16h32A8,8,0,0,1,208,168Zm-64,0a8,8,0,0,1-8,8H120a8,8,0,0,1,0-16h16A8,8,0,0,1,144,168Z"},null,-1),F=[O,R],L={key:2},q=n("path",{d:"M224,48H32A16,16,0,0,0,16,64V192a16,16,0,0,0,16,16H224a16,16,0,0,0,16-16V64A16,16,0,0,0,224,48ZM136,176H120a8,8,0,0,1,0-16h16a8,8,0,0,1,0,16Zm64,0H168a8,8,0,0,1,0-16h32a8,8,0,0,1,0,16ZM32,88V64H224V88Z"},null,-1),W=[q],Y={key:3},G=n("path",{d:"M224,50H32A14,14,0,0,0,18,64V192a14,14,0,0,0,14,14H224a14,14,0,0,0,14-14V64A14,14,0,0,0,224,50ZM32,62H224a2,2,0,0,1,2,2V90H30V64A2,2,0,0,1,32,62ZM224,194H32a2,2,0,0,1-2-2V102H226v90A2,2,0,0,1,224,194Zm-18-26a6,6,0,0,1-6,6H168a6,6,0,0,1,0-12h32A6,6,0,0,1,206,168Zm-64,0a6,6,0,0,1-6,6H120a6,6,0,0,1,0-12h16A6,6,0,0,1,142,168Z"},null,-1),J=[G],K={key:4},Q=n("path",{d:"M224,48H32A16,16,0,0,0,16,64V192a16,16,0,0,0,16,16H224a16,16,0,0,0,16-16V64A16,16,0,0,0,224,48Zm0,16V88H32V64Zm0,128H32V104H224v88Zm-16-24a8,8,0,0,1-8,8H168a8,8,0,0,1,0-16h32A8,8,0,0,1,208,168Zm-64,0a8,8,0,0,1-8,8H120a8,8,0,0,1,0-16h16A8,8,0,0,1,144,168Z"},null,-1),T=[Q],U={key:5},X=n("path",{d:"M224,52H32A12,12,0,0,0,20,64V192a12,12,0,0,0,12,12H224a12,12,0,0,0,12-12V64A12,12,0,0,0,224,52ZM32,60H224a4,4,0,0,1,4,4V92H28V64A4,4,0,0,1,32,60ZM224,196H32a4,4,0,0,1-4-4V100H228v92A4,4,0,0,1,224,196Zm-20-28a4,4,0,0,1-4,4H168a4,4,0,0,1,0-8h32A4,4,0,0,1,204,168Zm-64,0a4,4,0,0,1-4,4H120a4,4,0,0,1,0-8h16A4,4,0,0,1,140,168Z"},null,-1),a0=[X],e0={name:"PhCreditCard"},t0=b({...e0,props:{weight:{type:String},size:{type:[String,Number]},color:{type:String},mirrored:{type:Boolean}},setup(r){const e=r,d=p("weight","regular"),l=p("size","1em"),H=p("color","currentColor"),u=p("mirrored",!1),o=s(()=>{var a;return(a=e.weight)!=null?a:d}),m=s(()=>{var a;return(a=e.size)!=null?a:l}),V=s(()=>{var a;return(a=e.color)!=null?a:H}),h=s(()=>e.mirrored!==void 0?e.mirrored?"scale(-1, 1)":void 0:u?"scale(-1, 1)":void 0);return(a,o0)=>(t(),i("svg",M({xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 256 256",width:m.value,height:m.value,fill:V.value,transform:h.value},a.$attrs),[_(a.$slots,"default"),o.value==="bold"?(t(),i("g",$,E)):o.value==="duotone"?(t(),i("g",P,F)):o.value==="fill"?(t(),i("g",L,W)):o.value==="light"?(t(),i("g",Y,J)):o.value==="regular"?(t(),i("g",K,T)):o.value==="thin"?(t(),i("g",U,a0)):f("",!0)],16,D))}}),I0=b({__name:"Organization",setup(r){const d=z().params.organizationId,{result:l}=w(()=>S.get(d)),H=s(()=>l.value?[{label:"My organizations",path:"/organizations"},{label:l.value.name,path:`/organizations/${l.value.id}`}]:void 0),u=s(()=>{var m;return(m=l.value)==null?void 0:m.billingMetadata}),o=[{name:"Organization",items:[{name:"Projects",icon:B,path:"projects"},{name:"Editors",icon:I,path:"editors"},{name:"Billing",icon:t0,path:"billing"}]}];return(m,V)=>{const h=k("RouterView");return t(),v(y,null,{navbar:c(()=>[g(Z,{breadcrumb:H.value},null,8,["breadcrumb"])]),sidebar:c(()=>[g(N,{class:"sidebar",sections:o})]),content:c(()=>[g(A,null,{default:c(()=>[u.value?(t(),v(x,{key:0,"billing-metadata":u.value,"organization-id":C(d)},null,8,["billing-metadata","organization-id"])):f("",!0),g(h)]),_:1})]),_:1})}}});export{I0 as default};
//# sourceMappingURL=Organization.6c810f33.js.map
