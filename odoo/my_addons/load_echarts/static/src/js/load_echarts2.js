/** @odoo-module */
import { registry } from "@web/core/registry"


const { Component, onWillStart, useRef, onMounted } = owl

export class Owlkanban2 extends Component {
    setup(){

    }
}
Owlkanban2.template = "owl.Owlkanban2"
Owlkanban2.components = { }

registry.category("actions").add("load_echarts2.echarts_sale_order_template", Owlkanban2)