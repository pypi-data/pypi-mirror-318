var ye=Object.defineProperty;var fe=(s,e,a)=>e in s?ye(s,e,{enumerable:!0,configurable:!0,writable:!0,value:a}):s[e]=a;var P=(s,e,a)=>(fe(s,typeof e!="symbol"?e+"":e,a),a);import{a as G}from"./asyncComputed.b9262f9a.js";import{d as b,e as A,o as m,c as g,w as l,u as t,b as n,cS as M,aG as h,aB as q,cU as ge,bT as _,dj as he,E as T,cB as w,bL as N,cA as B,f as Y,Y as H,eb as ve,d7 as _e,e9 as we,aS as J,ep as Q,cG as W,ea as be,X as Ce,S as I,df as ke,dd as Ue}from"./index.313443c9.js";import{A as E}from"./index.1b040ba8.js";import{_ as Pe}from"./DocsButton.vue_vue_type_script_setup_true_lang.074935e5.js";import{A as F}from"./index.e8134b3d.js";import{C as ee}from"./CrudView.bd9ea3c2.js";import{G as te}from"./PhPencil.vue.6c477483.js";import{C as Re}from"./repository.7d5e5c19.js";import{C as R}from"./gateway.062e0276.js";import{E as ae}from"./record.7a34fecb.js";import{p as k}from"./popupNotifcation.b9f169b0.js";import{a as Z}from"./ant-design.8aa8f4c3.js";import{A as K,T as Ee}from"./TabPane.95a0dceb.js";import"./BookOutlined.3803112a.js";import"./Badge.eac660dd.js";import"./router.f4178cff.js";import"./url.c713496d.js";import"./PhDotsThreeVertical.vue.3db1f140.js";import"./index.87ed679d.js";import"./fetch.2ca01292.js";(function(){try{var s=typeof window<"u"?window:typeof global<"u"?global:typeof self<"u"?self:{},e=new Error().stack;e&&(s._sentryDebugIds=s._sentryDebugIds||{},s._sentryDebugIds[e]="0b211a5f-788c-4a64-a4c2-fd43eced556c",s._sentryDebugIdIdentifier="sentry-dbid-0b211a5f-788c-4a64-a4c2-fd43eced556c")}catch{}})();const Ae=b({__name:"View",props:{signupPolicy:{}},emits:["updated","save"],setup(s,{emit:e}){const a=s,o=A(a.signupPolicy.strategy),r=A(a.signupPolicy.strategy==="patternOnly"?a.signupPolicy.emailPatterns:[]),i=A(a.signupPolicy.strategy==="patternOnly"?a.signupPolicy.emailPatterns.map(c=>({label:c})):[]),y=c=>{const C=c;if(r.value=C,C.length===0){o.value="inviteOnly",f("inviteOnly");return}i.value=C.map(U=>({label:U})),a.signupPolicy.emailPatterns=c,e("updated",a.signupPolicy)},p=()=>{e("save")},f=c=>{o.value=c,c!=="patternOnly"&&(c==="inviteOnly"&&a.signupPolicy.allowOnlyInvited(),e("updated",a.signupPolicy))};return(c,C)=>(m(),g(t(he),{style:{"padding-top":"8px",width:"100%"},justify:"space-between",align:"flex-end"},{default:l(()=>[n(t(ge),{value:o.value,"onUpdate:value":f},{default:l(()=>[n(t(E),{direction:"vertical"},{default:l(()=>[n(t(M),{value:"inviteOnly"},{default:l(()=>[h("Allow listed users only")]),_:1}),n(t(E),null,{default:l(()=>[n(t(M),{value:"patternOnly"},{default:l(()=>[h("Allow everyone from this domain:")]),_:1}),n(t(q),{mode:"tags",value:c.signupPolicy.emailPatterns,style:{"min-width":"300px"},placeholder:"@domain.com or sub.domain.com",disabled:o.value!=="patternOnly",options:i.value,"dropdown-match-select-width":"",open:!1,"onUpdate:value":y},null,8,["value","disabled","options"])]),_:1})]),_:1})]),_:1},8,["value"]),n(t(_),{disabled:!c.signupPolicy.hasChanges,type:"primary",onClick:p},{default:l(()=>[h(" Save changes ")]),_:1},8,["disabled"])]),_:1}))}}),xe=b({__name:"NewUser",props:{roleOptions:{}},emits:["created","cancel"],setup(s,{emit:e}){const o=s.roleOptions.map(p=>({label:p.name,value:p.name})),r=T({email:"",roles:[]});function i(){e("cancel")}function y(){!r.email||e("created",r)}return(p,f)=>(m(),g(t(F),{open:"",title:"New user",width:720,"body-style":{paddingBottom:"80px"},"footer-style":{textAlign:"right"},onClose:i},{extra:l(()=>[n(t(E),null,{default:l(()=>[n(t(_),{onClick:i},{default:l(()=>[h("Cancel")]),_:1}),n(t(_),{type:"primary",onClick:y},{default:l(()=>[h("Submit")]),_:1})]),_:1})]),default:l(()=>[n(t(B),{model:r,layout:"vertical"},{default:l(()=>[n(t(w),{key:"email",label:"Email",required:!0},{default:l(()=>[n(t(N),{value:r.email,"onUpdate:value":f[0]||(f[0]=c=>r.email=c)},null,8,["value"])]),_:1}),n(t(w),{key:"role",label:"Role"},{default:l(()=>[n(t(q),{value:r.roles,"onUpdate:value":f[1]||(f[1]=c=>r.roles=c),mode:"multiple",options:t(o)},null,8,["value","options"])]),_:1})]),_:1},8,["model"])]),_:1}))}}),Oe=b({__name:"UpdateUser",props:{roleOptions:{},email:{},roles:{}},emits:["updated","cancel"],setup(s,{emit:e}){const a=s,o=a.roleOptions.map(p=>({label:p.name,value:p.name})),r=T({email:a.email,roles:a.roles});function i(){e("cancel")}function y(){e("updated",r)}return(p,f)=>(m(),g(t(F),{open:"",title:"Update user",width:720,"body-style":{paddingBottom:"80px"},"footer-style":{textAlign:"right"},onClose:i},{extra:l(()=>[n(t(E),null,{default:l(()=>[n(t(_),{onClick:i},{default:l(()=>[h("Cancel")]),_:1}),n(t(_),{type:"primary",onClick:y},{default:l(()=>[h("Submit")]),_:1})]),_:1})]),default:l(()=>[n(t(B),{model:r,layout:"vertical"},{default:l(()=>[n(t(w),{key:"email",label:"Email"},{default:l(()=>[n(t(N),{value:r.email,"onUpdate:value":f[0]||(f[0]=c=>r.email=c)},null,8,["value"])]),_:1}),n(t(w),{key:"role",label:"Role"},{default:l(()=>[n(t(q),{value:r.roles,"onUpdate:value":f[1]||(f[1]=c=>r.roles=c),mode:"multiple",options:t(o)},null,8,["value","options"])]),_:1})]),_:1},8,["model"])]),_:1}))}}),$e=b({__name:"View",props:{loading:{type:Boolean},users:{},onCreate:{type:Function},onEdit:{type:Function},onDelete:{type:Function}},setup(s){const e=s,a=Y(()=>{var o;return{columns:[{title:"Email"},{title:"Roles"},{title:"",align:"right"}],rows:(o=e.users.map(r=>({key:r.email,cells:[{type:"text",text:r.email},{type:"slot",key:"roles",payload:{roles:r.roles}},{type:"actions",actions:[{icon:te,label:"Edit",onClick:()=>e.onEdit(r)},{icon:Q,label:"Delete",onClick:()=>e.onDelete(r)}]}]})))!=null?o:[]}});return(o,r)=>(m(),g(ee,{"entity-name":"users",title:"",loading:o.loading,description:"List all app users.","empty-title":"No users yet",table:a.value,"create-button-text":"Add users",create:o.onCreate},{roles:l(({payload:i})=>[(m(!0),H(J,null,ve(i.roles,y=>(m(),g(t(_e),{key:y,bordered:""},{default:l(()=>[h(we(y),1)]),_:2},1024))),128))]),_:1},8,["loading","table","create"]))}}),De=b({__name:"NewRole",emits:["created","cancel"],setup(s,{emit:e}){const a=T({name:"",description:""});function o(){e("cancel")}function r(){!a.name||e("created",a)}return(i,y)=>(m(),g(t(F),{open:"",title:"New role",width:720,"body-style":{paddingBottom:"80px"},"footer-style":{textAlign:"right"},onClose:o},{extra:l(()=>[n(t(E),null,{default:l(()=>[n(t(_),{onClick:o},{default:l(()=>[h("Cancel")]),_:1}),n(t(_),{type:"primary",onClick:r},{default:l(()=>[h("Submit")]),_:1})]),_:1})]),default:l(()=>[n(t(B),{model:a,layout:"vertical"},{default:l(()=>[n(t(w),{key:"name",label:"Name",required:!0},{default:l(()=>[n(t(N),{value:a.name,"onUpdate:value":y[0]||(y[0]=p=>a.name=p)},null,8,["value"])]),_:1}),n(t(w),{key:"description",label:"Description"},{default:l(()=>[n(t(W),{value:a.description,"onUpdate:value":y[1]||(y[1]=p=>a.description=p),placeholder:"Optional description",rows:3},null,8,["value"])]),_:1})]),_:1},8,["model"])]),_:1}))}}),Ie=b({__name:"UpdateRole",props:{name:{},description:{}},emits:["updated","cancel"],setup(s,{emit:e}){const a=s,o=T({description:a.description});function r(){e("cancel")}function i(){e("updated",o)}return(y,p)=>(m(),g(t(F),{open:"",title:"Update role",width:720,"body-style":{paddingBottom:"80px"},"footer-style":{textAlign:"right"},onClose:r},{extra:l(()=>[n(t(E),null,{default:l(()=>[n(t(_),{onClick:r},{default:l(()=>[h("Cancel")]),_:1}),n(t(_),{type:"primary",onClick:i},{default:l(()=>[h("Submit")]),_:1})]),_:1})]),default:l(()=>[n(t(B),{model:o,layout:"vertical"},{default:l(()=>[n(t(w),{key:"name",label:"Name"},{default:l(()=>[n(t(N),{value:a.name,disabled:""},null,8,["value"])]),_:1}),n(t(w),{key:"role",label:"Role"},{default:l(()=>[n(t(W),{value:o.description,"onUpdate:value":p[0]||(p[0]=f=>o.description=f),placeholder:"Optional description",rows:3},null,8,["value"])]),_:1})]),_:1},8,["model"])]),_:1}))}}),je=b({__name:"View",props:{loading:{type:Boolean},roles:{},onCreate:{type:Function},onEdit:{type:Function},onDelete:{type:Function}},setup(s){const e=s,a=Y(()=>{var o;return{columns:[{title:"Name"},{title:"Description"},{title:"",align:"right"}],rows:(o=e.roles.map(r=>({key:r.id,cells:[{type:"text",text:r.name},{type:"text",text:r.description},{type:"actions",actions:[{icon:te,label:"Edit",onClick:()=>e.onEdit(r)},{icon:Q,label:"Delete",onClick:()=>e.onDelete(r)}]}]})))!=null?o:[]}});return(o,r)=>(m(),g(ee,{"entity-name":"roles",loading:o.loading,title:"",description:"List all app roles.","empty-title":"No roles yet",table:a.value,"create-button-text":"Add roles",create:o.onCreate},null,8,["loading","table","create"]))}}),S=class{constructor(e){P(this,"record");this.dto=e,this.record=ae.from(e)}static from(e){return new S(e)}toDTO(){return this.record.toDTO()}get id(){return this.record.get("id")}get projectId(){return this.record.get("projectId")}get emailPatterns(){return this.record.get("emailPatterns")}set emailPatterns(e){this.record.set("emailPatterns",e)}get hasChanges(){return this.record.hasChangesDeep("emailPatterns")}get strategy(){return this.dto.emailPatterns.length===0?"inviteOnly":"patternOnly"}get changes(){return this.record.changes}allowOnlyInvited(){this.record.set("emailPatterns",[])}static validate(e){return S.pattern.test(e)}};let x=S;P(x,"pattern",new RegExp("^@?(?!-)[A-Za-z0-9-]{1,}(?<!-)(\\.[A-Za-z]{2,})+$"));class Se{constructor(){P(this,"urlPath","signup-policy")}async update(e,a){return R.patch(`projects/${e}/${this.urlPath}`,a)}async get(e){return R.get(`projects/${e}/${this.urlPath}`)}}const X=new Se;class Te{constructor(e){this.projectId=e}async update(e){const{emailPatterns:a}=e.changes;if(!a)return e;const o=await X.update(this.projectId,{emailPatterns:a});return x.from(o)}async get(){const e=await X.get(this.projectId);return x.from(e)}}class z{constructor(e){P(this,"record");this.dto=e,this.record=ae.from(e)}static from(e){return new z(e)}toDTO(){return this.record.toDTO()}get changes(){return this.record.changes}get id(){return this.record.get("id")}get email(){return this.record.get("email")}set email(e){this.record.set("email",e)}get projectId(){return this.record.get("projectId")}get roles(){return this.record.get("roles")}set roles(e){this.record.set("roles",e)}update(e){this.record.update(e)}resetChanges(){this.record.resetChanges()}}class Ne{constructor(){P(this,"urlPath","users")}async create(e,a){return R.post(`projects/${e}/${this.urlPath}`,a)}async delete(e,a){await R.delete(`projects/${e}/${this.urlPath}/${a}`)}async list(e,{limit:a,offset:o}){const r={};a&&(r.limit=a.toString()),o&&(r.offset=o.toString());const i=new URLSearchParams(r);return R.get(`projects/${e}/${this.urlPath}?${i.toString()}`)}async update(e,a,o){return R.patch(`projects/${e}/${this.urlPath}/${a}`,o)}}const j=new Ne;class Be{constructor(e){this.projectId=e}async create(e){await j.create(this.projectId,e)}async update(e,a){await j.update(this.projectId,e,a)}async delete(e){await j.delete(this.projectId,e)}async list(e,a){return(await j.list(this.projectId,{limit:e,offset:a})).map(z.from)}}const lt=b({__name:"View",setup(s){const a=be().params.projectId,o=A({type:"initial"}),r=A("users");Ce(()=>{const d=new URLSearchParams(location.search).get("selected-panel")||"users",v=["roles","users"].includes(d)?d:"users";d&&(r.value=v)});const i=()=>{o.value.type="initial"},y=()=>{o.value.type="creatingUser"},p=u=>{o.value={type:"editingUser",payload:u}},f=()=>{o.value.type="creatingRole"},c=u=>{o.value={type:"editingRole",payload:u}},C=new Te(a),{result:U,refetch:oe}=G(()=>C.get()),re=async()=>{if(!!U.value)try{await C.update(U.value),oe()}catch(u){u instanceof Error&&k("Update Error",u.message)}},O=new Be(a),{loading:ne,result:le,refetch:$}=G(()=>O.list(100,0)),D=new Re(a),{loading:se,result:V,refetch:L}=G(()=>D.list(100,0)),ie=async u=>{try{if(o.value.type!=="creatingUser")return;await O.create(u),i(),$()}catch(d){d instanceof Error&&k("Create Error",d.message)}},ce=async u=>{try{if(o.value.type!=="editingUser")return;await O.update(o.value.payload.id,u),i(),$()}catch(d){d instanceof Error&&k("Update Error",d.message)}},ue=async u=>{if(!!await Z("Deleting users revoke their access to your application (in case they aren't allowed by a domain rule). Are you sure you want to continue?"))try{await O.delete(u.id),$()}catch(v){v instanceof Error&&k("Delete Error",v.message)}},de=async u=>{try{if(o.value.type!=="creatingRole")return;await D.create(u),i(),L()}catch(d){d instanceof Error&&k("Create Error",d.message)}},pe=async u=>{try{if(o.value.type!=="editingRole")return;await D.update(o.value.payload.id,u),i(),L()}catch(d){d instanceof Error&&k("Update Error",d.message)}},me=async u=>{if(!!await Z("Deleteing roles may revoke access to some features in your application. Are you sure you want to continue?"))try{await D.delete(u.id),L(),$()}catch(v){v instanceof Error&&k("Delete Error",v.message)}};return(u,d)=>(m(),H(J,null,[n(t(ke),null,{default:l(()=>[h("Access Control")]),_:1}),n(t(Ue),null,{default:l(()=>[h(" Manage how your end users interect with your application. "),n(Pe,{path:"concepts/access-control"})]),_:1}),n(t(Ee),{"active-key":r.value,"onUpdate:activeKey":d[0]||(d[0]=v=>r.value=v)},{default:l(()=>[n(t(K),{key:"users",tab:"Users"}),n(t(K),{key:"roles",tab:"Roles"})]),_:1},8,["active-key"]),r.value==="users"&&t(U)?(m(),g(Ae,{key:0,"signup-policy":t(U),onSave:re},null,8,["signup-policy"])):I("",!0),r.value==="users"?(m(),g($e,{key:1,loading:t(ne),users:t(le)||[],onCreate:y,onEdit:p,onDelete:ue},null,8,["loading","users"])):I("",!0),r.value==="roles"?(m(),g(je,{key:2,loading:t(se),roles:t(V)||[],onCreate:f,onEdit:c,onDelete:me},null,8,["loading","roles"])):I("",!0),o.value.type==="creatingUser"?(m(),g(xe,{key:3,"role-options":t(V)||[],onCancel:i,onCreated:ie},null,8,["role-options"])):o.value.type==="editingUser"?(m(),g(Oe,{key:4,email:o.value.payload.email,roles:o.value.payload.roles||[],"role-options":t(V)||[],onUpdated:ce,onCancel:i},null,8,["email","roles","role-options"])):o.value.type==="creatingRole"?(m(),g(De,{key:5,onCancel:i,onCreated:de})):o.value.type==="editingRole"?(m(),g(Ie,{key:6,name:o.value.payload.name,description:o.value.payload.description,onUpdated:pe,onCancel:i},null,8,["name","description"])):I("",!0)],64))}});export{lt as default};
//# sourceMappingURL=View.b0bd63aa.js.map
