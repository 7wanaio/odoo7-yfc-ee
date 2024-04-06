/** @odoo-module */

import {registry} from "@web/core/registry";
import { ListController } from "@web/views/list/list_controller";
import { listView } from "@web/views/list/list_view";
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

class CsListController extends ListController {
    setup() {
        super.setup();
        this.orm = useService("orm");
        this.notificationService = useService("notification");

        onMounted(() => {
            $('#tree').treeview({data: nestdata});
        });
    }


}

CsListController.template = "cs.ListView";

export const CsListView = {
    ...listView,
    Controller: CsListController,
};

registry.category("views").add("cs_list_view", CsListView);