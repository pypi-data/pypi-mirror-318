import{L as C}from"./CircularLoading.b705d06b.js";import{d as P,e as B,o as c,Y as h,a as v,b as n,e9 as r,u as a,c as b,w as u,S as q,eP as t,bL as I,eO as A,cB as T,aG as m,bT as p,cA as L,a0 as R,eo as D,ea as $,f as K,dF as N}from"./index.313443c9.js";import{_ as S}from"./AbstraLogo.vue_vue_type_script_setup_true_lang.5f0d7dd4.js";import{T as V,A as F}from"./router.f4178cff.js";import{i as U}from"./string.1aa5755a.js";import{a as y,E as M}from"./gateway.062e0276.js";import"./Logo.4dd4184b.js";import"./Badge.eac660dd.js";import"./popupNotifcation.b9f169b0.js";(function(){try{var l=typeof window<"u"?window:typeof global<"u"?global:typeof self<"u"?self:{},s=new Error().stack;s&&(l._sentryDebugIds=l._sentryDebugIds||{},l._sentryDebugIds[s]="1572ef90-e97c-4bf2-9b44-4b793d54b267",l._sentryDebugIdIdentifier="sentry-dbid-1572ef90-e97c-4bf2-9b44-4b793d54b267")}catch{}})();const O={class:"form"},j={class:"header"},z={class:"description"},G={class:"description"},Y={class:"footer"},H={key:2,class:"loading"},J=P({__name:"Passwordless",emits:["done"],setup(l,{emit:s}){const e=B({stage:"collect-info",info:{email:""},token:"",invalid:!1,secsToAllowResend:0});function _(){const i=e.value.info.email,o=U(i);return e.value.invalid=!o,o}let d;const f=async()=>{if(!!_()){e.value.stage="loading";try{await y.authenticate(e.value.info.email),e.value.stage="collect-token",e.value.secsToAllowResend=120,clearInterval(d),d=setInterval(()=>{e.value.secsToAllowResend-=1,e.value.secsToAllowResend<=0&&clearInterval(d)},1e3)}catch{e.value.invalid=!0,e.value.stage="collect-info"}}},k=i=>{if(!i){e.value.info.email="";return}e.value.info.email=i.toLowerCase()},w=async()=>{var i;if(!!((i=e.value.info)!=null&&i.email)){e.value.stage="loading";try{const o=await y.verify(e.value.info.email,e.value.token);if(!o)throw new Error("[Passwordless] Login did not return an user");V.trackSession(),s("done",o),e.value.stage="done"}catch{e.value.invalid=!0,e.value.stage="collect-token"}}},x=()=>{e.value.info&&f()},E=()=>{e.value.stage="collect-info",e.value.info={email:""},e.value.token="",e.value.invalid=!1};return(i,o)=>(c(),h("div",O,[v("div",j,[n(S,{"hide-text":"",size:"large"}),v("h2",null,r(a(t).translate("i18n_auth_validate_your_email_login",null,{brandName:"Abstra"})),1)]),e.value.stage==="collect-info"?(c(),b(a(L),{key:0,class:"section"},{default:u(()=>[v("div",z,r(a(t).translate("i18n_auth_info_description")),1),n(a(T),{"has-feedback":"","validate-status":e.value.invalid?"error":"",help:e.value.invalid?a(t).translate("i18n_auth_info_invalid_email"):""},{default:u(()=>[n(a(I),{type:"email",value:e.value.info.email,placeholder:a(t).translate("i18n_auth_enter_your_work_email"),onBlur:_,onKeyup:A(f,["enter"]),onChange:o[0]||(o[0]=g=>k(g.target.value))},null,8,["value","placeholder","onKeyup"])]),_:1},8,["validate-status","help"]),n(a(p),{type:"primary",onClick:f},{default:u(()=>[m(r(a(t).translate("i18n_auth_info_send_code")),1)]),_:1})]),_:1})):e.value.stage==="collect-token"?(c(),b(a(L),{key:1,class:"section"},{default:u(()=>[v("div",G,r(a(t).translate("i18n_auth_token_label",null,e.value.info)),1),n(a(T),{"has-feedback":"","validate-status":e.value.invalid?"error":"",help:e.value.invalid?a(t).translate("i18n_auth_token_invalid"):""},{default:u(()=>[n(a(I),{value:e.value.token,"onUpdate:value":o[1]||(o[1]=g=>e.value.token=g),type:"number",placeholder:a(t).translate("i18n_auth_enter_your_token"),onKeyup:A(w,["enter"])},null,8,["value","placeholder","onKeyup"])]),_:1},8,["validate-status","help"]),n(a(p),{type:"primary",onClick:w},{default:u(()=>[m(r(a(t).translate("i18n_auth_token_verify_email")),1)]),_:1}),n(a(p),{onClick:E},{default:u(()=>[m(r(a(t).translate("i18n_auth_edit_email")),1)]),_:1}),n(a(p),{disabled:!!e.value.secsToAllowResend,onClick:x},{default:u(()=>[m(r(a(t).translate("i18n_auth_token_resend_email"))+" ("+r(e.value.secsToAllowResend)+" s) ",1)]),_:1},8,["disabled"]),v("div",Y,r(a(t).translate("i18n_auth_token_footer_alternative_email")),1)]),_:1})):e.value.stage==="loading"?(c(),h("div",H,[n(C)])):q("",!0)]))}});const Q=R(J,[["__scopeId","data-v-b9707eaf"]]),W=async()=>{const l=y.getAuthor();if(!l)return;const{status:s}=await F.getInfo();if(s==="active")return;const e=new URLSearchParams({token:l.jwt,status:s});window.location.replace(`${M.onboarding}/setup?${e}`)},X={key:0,class:"login"},Z={key:1,class:"loading"},ee=P({__name:"Login",setup(l){const s=D(),e=$();async function _(){await W(),e.query.redirect?await s.push({path:e.query.redirect,query:{...e.query,redirect:e.query["prev-redirect"],"prev-redirect":void 0}}):s.push({name:"home"})}const d=K(()=>!y.getAuthor());return N(()=>{d.value||_()}),(f,k)=>d.value?(c(),h("div",X,[n(Q,{onDone:_})])):(c(),h("div",Z,[n(C)]))}});const de=R(ee,[["__scopeId","data-v-e4e9b925"]]);export{de as default};
//# sourceMappingURL=Login.c7f7029c.js.map
