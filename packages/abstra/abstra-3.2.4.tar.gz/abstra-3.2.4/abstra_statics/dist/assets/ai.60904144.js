import"./index.fd9b9ab8.js";(function(){try{var a=typeof window<"u"?window:typeof global<"u"?global:typeof self<"u"?self:{},e=new Error().stack;e&&(a._sentryDebugIds=a._sentryDebugIds||{},a._sentryDebugIds[e]="eb6e240e-b9b2-492a-b22f-dfc28b39a895",a._sentryDebugIdIdentifier="sentry-dbid-eb6e240e-b9b2-492a-b22f-dfc28b39a895")}catch{}})();class p{static async*sendMessage(e,t,o,n){var i;const s=await fetch("/_editor/api/ai/message",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({messages:e,runtime:t,threadId:o})});if(!s.ok)throw new Error("Failed to send message");const r=(i=s.body)==null?void 0:i.getReader();if(!r)throw new Error("No response body");for(;!n();){const d=await r.read();if(d.done)break;yield new TextDecoder().decode(d.value)}}static async createThread(){return(await fetch("/_editor/api/ai/thread",{method:"POST"})).json()}static async cancelAllRuns(e){return(await fetch("/_editor/api/ai/cancel-all",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({threadId:e})})).ok}static async generateProject(e){const t=await fetch("/_editor/api/ai/generate",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({prompt:e})});if(!t.ok){const o=await t.text();throw new Error(o)}}static async vote(e,t,o,n){await fetch("/_editor/api/ai/vote",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({vote:e,question:t,answer:o,context:n})})}}export{p as A};
//# sourceMappingURL=ai.60904144.js.map
