import{b7 as N,aN as v,aO as S,av as R,aM as j,ad as J,ae as Q,dU as Y,U as w,bi as ee,ap as ne,d as z,aq as X,e as oe,dV as ae,g as te,ai as F,f as le,aj as T,b as f,al as k,dW as se,aD as re,dI as ie,dX as de,aF as V,bu as ce,aA as pe,R as ue,aL as fe,c8 as be,a_ as ve,aZ as ge,a$ as $e}from"./index.313443c9.js";(function(){try{var n=typeof window<"u"?window:typeof global<"u"?global:typeof self<"u"?self:{},e=new Error().stack;e&&(n._sentryDebugIds=n._sentryDebugIds||{},n._sentryDebugIds[e]="70cdeb88-4ec5-4ee8-b338-34b9cd81f643",n._sentryDebugIdIdentifier="sentry-dbid-70cdeb88-4ec5-4ee8-b338-34b9cd81f643")}catch{}})();const me=()=>({prefixCls:String,activeKey:N([Array,Number,String]),defaultActiveKey:N([Array,Number,String]),accordion:v(),destroyInactivePanel:v(),bordered:v(),expandIcon:S(),openAnimation:R.object,expandIconPosition:j(),collapsible:j(),ghost:v(),onChange:S(),"onUpdate:activeKey":S()}),G=()=>({openAnimation:R.object,prefixCls:String,header:R.any,headerClass:String,showArrow:v(),isActive:v(),destroyInactivePanel:v(),disabled:v(),accordion:v(),forceRender:v(),expandIcon:S(),extra:R.any,panelKey:N(),collapsible:j(),role:String,onItemClick:S()}),ye=n=>{const{componentCls:e,collapseContentBg:a,padding:p,collapseContentPaddingHorizontal:i,collapseHeaderBg:d,collapseHeaderPadding:l,collapsePanelBorderRadius:u,lineWidth:b,lineType:$,colorBorder:x,colorText:h,colorTextHeading:g,colorTextDisabled:m,fontSize:C,lineHeight:y,marginSM:A,paddingSM:o,motionDurationSlow:t,fontSizeIcon:s}=n,r=`${b}px ${$} ${x}`;return{[e]:w(w({},ne(n)),{backgroundColor:d,border:r,borderBottom:0,borderRadius:`${u}px`,["&-rtl"]:{direction:"rtl"},[`& > ${e}-item`]:{borderBottom:r,["&:last-child"]:{[`
            &,
            & > ${e}-header`]:{borderRadius:`0 0 ${u}px ${u}px`}},[`> ${e}-header`]:{position:"relative",display:"flex",flexWrap:"nowrap",alignItems:"flex-start",padding:l,color:g,lineHeight:y,cursor:"pointer",transition:`all ${t}, visibility 0s`,[`> ${e}-header-text`]:{flex:"auto"},"&:focus":{outline:"none"},[`${e}-expand-icon`]:{height:C*y,display:"flex",alignItems:"center",paddingInlineEnd:A},[`${e}-arrow`]:w(w({},ee()),{fontSize:s,svg:{transition:`transform ${t}`}}),[`${e}-header-text`]:{marginInlineEnd:"auto"}},[`${e}-header-collapsible-only`]:{cursor:"default",[`${e}-header-text`]:{flex:"none",cursor:"pointer"},[`${e}-expand-icon`]:{cursor:"pointer"}},[`${e}-icon-collapsible-only`]:{cursor:"default",[`${e}-expand-icon`]:{cursor:"pointer"}},[`&${e}-no-arrow`]:{[`> ${e}-header`]:{paddingInlineStart:o}}},[`${e}-content`]:{color:h,backgroundColor:a,borderTop:r,[`& > ${e}-content-box`]:{padding:`${p}px ${i}px`},["&-hidden"]:{display:"none"}},[`${e}-item:last-child`]:{[`> ${e}-content`]:{borderRadius:`0 0 ${u}px ${u}px`}},[`& ${e}-item-disabled > ${e}-header`]:{[`
          &,
          & > .arrow
        `]:{color:m,cursor:"not-allowed"}},[`&${e}-icon-position-end`]:{[`& > ${e}-item`]:{[`> ${e}-header`]:{[`${e}-expand-icon`]:{order:1,paddingInlineEnd:0,paddingInlineStart:A}}}}})}},xe=n=>{const{componentCls:e}=n,a=`> ${e}-item > ${e}-header ${e}-arrow svg`;return{[`${e}-rtl`]:{[a]:{transform:"rotate(180deg)"}}}},he=n=>{const{componentCls:e,collapseHeaderBg:a,paddingXXS:p,colorBorder:i}=n;return{[`${e}-borderless`]:{backgroundColor:a,border:0,[`> ${e}-item`]:{borderBottom:`1px solid ${i}`},[`
        > ${e}-item:last-child,
        > ${e}-item:last-child ${e}-header
      `]:{borderRadius:0},[`> ${e}-item:last-child`]:{borderBottom:0},[`> ${e}-item > ${e}-content`]:{backgroundColor:"transparent",borderTop:0},[`> ${e}-item > ${e}-content > ${e}-content-box`]:{paddingTop:p}}}},Ce=n=>{const{componentCls:e,paddingSM:a}=n;return{[`${e}-ghost`]:{backgroundColor:"transparent",border:0,[`> ${e}-item`]:{borderBottom:0,[`> ${e}-content`]:{backgroundColor:"transparent",border:0,[`> ${e}-content-box`]:{paddingBlock:a}}}}}},Ae=J("Collapse",n=>{const e=Q(n,{collapseContentBg:n.colorBgContainer,collapseHeaderBg:n.colorFillAlter,collapseHeaderPadding:`${n.paddingSM}px ${n.padding}px`,collapsePanelBorderRadius:n.borderRadiusLG,collapseContentPaddingHorizontal:16});return[ye(e),he(e),Ce(e),xe(e),Y(e)]});function W(n){let e=n;if(!Array.isArray(e)){const a=typeof e;e=a==="number"||a==="string"?[e]:[]}return e.map(a=>String(a))}const Se=z({compatConfig:{MODE:3},name:"ACollapse",inheritAttrs:!1,props:X(me(),{accordion:!1,destroyInactivePanel:!1,bordered:!0,expandIconPosition:"start"}),slots:Object,setup(n,e){let{attrs:a,slots:p,emit:i}=e;const d=oe(W(ae([n.activeKey,n.defaultActiveKey])));te(()=>n.activeKey,()=>{d.value=W(n.activeKey)},{deep:!0});const{prefixCls:l,direction:u,rootPrefixCls:b}=F("collapse",n),[$,x]=Ae(l),h=le(()=>{const{expandIconPosition:o}=n;return o!==void 0?o:u.value==="rtl"?"end":"start"}),g=o=>{const{expandIcon:t=p.expandIcon}=n,s=t?t(o):f(ce,{rotate:o.isActive?90:void 0},null);return f("div",{class:[`${l.value}-expand-icon`,x.value],onClick:()=>["header","icon"].includes(n.collapsible)&&C(o.panelKey)},[pe(Array.isArray(t)?s[0]:s)?V(s,{class:`${l.value}-arrow`},!1):s])},m=o=>{n.activeKey===void 0&&(d.value=o);const t=n.accordion?o[0]:o;i("update:activeKey",t),i("change",t)},C=o=>{let t=d.value;if(n.accordion)t=t[0]===o?[]:[o];else{t=[...t];const s=t.indexOf(o);s>-1?t.splice(s,1):t.push(o)}m(t)},y=(o,t)=>{var s,r,I;if(ie(o))return;const c=d.value,{accordion:P,destroyInactivePanel:E,collapsible:K,openAnimation:_}=n,D=_||de(`${b.value}-motion-collapse`),B=String((s=o.key)!==null&&s!==void 0?s:t),{header:L=(I=(r=o.children)===null||r===void 0?void 0:r.header)===null||I===void 0?void 0:I.call(r),headerClass:q,collapsible:H,disabled:U}=o.props||{};let M=!1;P?M=c[0]===B:M=c.indexOf(B)>-1;let O=H!=null?H:K;(U||U==="")&&(O="disabled");const Z={key:B,panelKey:B,header:L,headerClass:q,isActive:M,prefixCls:l.value,destroyInactivePanel:E,openAnimation:D,accordion:P,onItemClick:O==="disabled"?null:C,expandIcon:g,collapsible:O};return V(o,Z)},A=()=>{var o;return re((o=p.default)===null||o===void 0?void 0:o.call(p)).map(y)};return()=>{const{accordion:o,bordered:t,ghost:s}=n,r=T(l.value,{[`${l.value}-borderless`]:!t,[`${l.value}-icon-position-${h.value}`]:!0,[`${l.value}-rtl`]:u.value==="rtl",[`${l.value}-ghost`]:!!s,[a.class]:!!a.class},x.value);return $(f("div",k(k({class:r},se(a)),{},{style:a.style,role:o?"tablist":null}),[A()]))}}}),Ie=z({compatConfig:{MODE:3},name:"PanelContent",props:G(),setup(n,e){let{slots:a}=e;const p=ue(!1);return fe(()=>{(n.isActive||n.forceRender)&&(p.value=!0)}),()=>{var i;if(!p.value)return null;const{prefixCls:d,isActive:l,role:u}=n;return f("div",{class:T(`${d}-content`,{[`${d}-content-active`]:l,[`${d}-content-inactive`]:!l}),role:u},[f("div",{class:`${d}-content-box`},[(i=a.default)===null||i===void 0?void 0:i.call(a)])])}}}),Pe=z({compatConfig:{MODE:3},name:"ACollapsePanel",inheritAttrs:!1,props:X(G(),{showArrow:!0,isActive:!1,onItemClick(){},headerClass:"",forceRender:!1}),slots:Object,setup(n,e){let{slots:a,emit:p,attrs:i}=e;be(n.disabled===void 0,"Collapse.Panel",'`disabled` is deprecated. Please use `collapsible="disabled"` instead.');const{prefixCls:d}=F("collapse",n),l=()=>{p("itemClick",n.panelKey)},u=b=>{(b.key==="Enter"||b.keyCode===13||b.which===13)&&l()};return()=>{var b,$;const{header:x=(b=a.header)===null||b===void 0?void 0:b.call(a),headerClass:h,isActive:g,showArrow:m,destroyInactivePanel:C,accordion:y,forceRender:A,openAnimation:o,expandIcon:t=a.expandIcon,extra:s=($=a.extra)===null||$===void 0?void 0:$.call(a),collapsible:r}=n,I=r==="disabled",c=d.value,P=T(`${c}-header`,{[h]:h,[`${c}-header-collapsible-only`]:r==="header",[`${c}-icon-collapsible-only`]:r==="icon"}),E=T({[`${c}-item`]:!0,[`${c}-item-active`]:g,[`${c}-item-disabled`]:I,[`${c}-no-arrow`]:!m,[`${i.class}`]:!!i.class});let K=f("i",{class:"arrow"},null);m&&typeof t=="function"&&(K=t(n));const _=ve(f(Ie,{prefixCls:c,isActive:g,forceRender:A,role:y?"tabpanel":null},{default:a.default}),[[$e,g]]),D=w({appear:!1,css:!1},o);return f("div",k(k({},i),{},{class:E}),[f("div",{class:P,onClick:()=>!["header","icon"].includes(r)&&l(),role:y?"tab":"button",tabindex:I?-1:0,"aria-expanded":g,onKeypress:u},[m&&K,f("span",{onClick:()=>r==="header"&&l(),class:`${c}-header-text`},[x]),s&&f("div",{class:`${c}-extra`},[s])]),f(ge,D,{default:()=>[!C||g?_:null]})])}}});export{Pe as A,Se as C};
//# sourceMappingURL=CollapsePanel.5d2add1e.js.map
