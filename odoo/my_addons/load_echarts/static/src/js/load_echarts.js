/** @odoo-module */
import { registry } from "@web/core/registry"


const { Component, onWillStart, useRef, onMounted } = owl
export class Owlkanban1 extends Component {
    setup(){
        

    }
}
Owlkanban1.template = "owl.Owlkanban1"
Owlkanban1.components = { }

registry.category("actions").add("load_echarts.echarts_stock_template", Owlkanban1)

