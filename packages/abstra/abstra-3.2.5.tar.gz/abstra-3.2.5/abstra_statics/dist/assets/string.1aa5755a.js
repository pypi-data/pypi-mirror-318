import{O as l}from"./index.313443c9.js";(function(){try{var e=typeof window<"u"?window:typeof global<"u"?global:typeof self<"u"?self:{},n=new Error().stack;n&&(e._sentryDebugIds=e._sentryDebugIds||{},e._sentryDebugIds[n]="39ccab44-c8cb-4027-8533-7b4ee117ec97",e._sentryDebugIdIdentifier="sentry-dbid-39ccab44-c8cb-4027-8533-7b4ee117ec97")}catch{}})();function f(e){return l.string().email().safeParse(e).success}function d(e){return e.charAt(0).toUpperCase()+e.slice(1)}function g(e,n,r=!1,c=!0,a=!1){const o=(c?e.toLocaleLowerCase():e).normalize("NFD").replace(/[\u0300-\u036f]/g,""),s=a?o.replace(/[^a-zA-Z0-9/]/g,"_"):o.replace(/[^a-zA-Z0-9]/g,"_"),i=r?s:s.replace(/_+/g,"_");return n?i:i.replace(/_$/,"")}function b(e){var t;const r=e.toLocaleLowerCase().trim().normalize("NFD").replace(/[\u0300-\u036f]/g,""),c=/[a-z0-9]+/g,a=r.match(c);return(t=a==null?void 0:a.join("-"))!=null?t:""}export{b as a,d as c,f as i,g as n};
//# sourceMappingURL=string.1aa5755a.js.map
