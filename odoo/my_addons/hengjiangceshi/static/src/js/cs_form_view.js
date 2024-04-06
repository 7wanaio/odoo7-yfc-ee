/** @odoo-module */

import {registry} from "@web/core/registry";
import {FormController} from "@web/views/form/form_controller";
import {formView} from "@web/views/form/form_view";
import {useService} from "@web/core/utils/hooks";
import {useDebounced} from "@web/core/utils/timing";
const { Component, onMounted } = owl;

var nestdata = [
  {
    text: "型号",
    nodes: [
      {
        text: "Child 1",
        nodes: [
          {
            text: "Grandchild 1"
          },
          {
            text: "Grandchild 2"
          }
        ]
      },
      {
        text: "Child 2"
      }
    ]
  },
  {
    text: "Parent 2"
  },
  {
    text: "Parent 3"
  },
  {
    text: "Parent 4"
  },
  {
    text: "Parent 5"
  }
];

class CsFormController extends FormController {
    setup() {
        super.setup();
        this.orm = useService("orm");
        this.notificationService = useService("notification");

        onMounted(() => {
            $('#tree').treeview({data: nestdata});
        });
    }


}

CsFormController.template = "cs.FormView";

export const CsFormView = {
    ...formView,
    Controller: CsFormController,
};

registry.category("views").add("cs_form_view", CsFormView);