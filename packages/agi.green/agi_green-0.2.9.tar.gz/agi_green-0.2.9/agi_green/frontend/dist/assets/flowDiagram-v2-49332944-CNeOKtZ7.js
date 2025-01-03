import { p as parser$1, f as flowDb } from "./flowDb-d35e309a-CxPTbR9R.js";
import { f as flowRendererV2, g as flowStyles } from "./styles-7383a064-CX4mV7_t.js";
import { t as setConfig } from "./index-B6VDnkkC.js";
import "./graph-BZLDNLYU.js";
import "./layout-C62H5oXw.js";
import "./index-8fae9850-D4CV6lij.js";
import "./clone-qct2WtQa.js";
import "./edges-d417c7a0-C1vtNQ74.js";
import "./createText-423428c9-DQoEU2lB.js";
import "./line-D-9O3gIk.js";
import "./array-DgktLKBx.js";
import "./path-Cp2qmpkd.js";
import "./channel-BEnAz4vm.js";
const diagram = {
  parser: parser$1,
  db: flowDb,
  renderer: flowRendererV2,
  styles: flowStyles,
  init: (cnf) => {
    if (!cnf.flowchart) {
      cnf.flowchart = {};
    }
    cnf.flowchart.arrowMarkerAbsolute = cnf.arrowMarkerAbsolute;
    setConfig({ flowchart: { arrowMarkerAbsolute: cnf.arrowMarkerAbsolute } });
    flowRendererV2.setConf(cnf.flowchart);
    flowDb.clear();
    flowDb.setGen("gen-2");
  }
};
export {
  diagram
};
//# sourceMappingURL=flowDiagram-v2-49332944-CNeOKtZ7.js.map
