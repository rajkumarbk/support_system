/** @odoo-module */

import { registry } from "@web/core/registry";
import { KpiCard,CustomerCard } from "./kpi_card/kpi_card";
import { ChartRenderer } from "./chart_renderer/chart_renderer";
import { loadJS } from "@web/core/assets";
import { useService } from "@web/core/utils/hooks";
const { Component, onWillStart, useRef, onMounted, useState } = owl;

export class OwlReportingDashboard extends Component {
    setup() {
        this.state = owl.useState({
            problem: {
                value: 5,
                percentage:10,
                finished:1,
                fresh:1,
                progress:1,
            }
        });

        this.orm = useService("orm");

        onWillStart(async () => {
            await this.getTotalUsers();
            await this.getTotalClosedUsers();
            await this.getFreshNewUsers();
            await this.getTotalProgressUsers();


        });
    }

    async getTotalUsers() {
        try {
            const totalUsers = await this.orm.searchCount("support_sys.support_sys", [])
            this.state.problem.value = totalUsers;
        } catch (error) {
        console.error("Error fetching total users:", error);
        }
    }
    async getTotalClosedUsers() {
        try {
            const domain = [['status', '=', 'closed']]; // Define domain to filter records
            const totalClosedUsers = await this.orm.searchCount("support_sys.support_sys", domain);
            this.state.problem.finished = totalClosedUsers;
        } catch (error) {
            console.error("Error fetching total closed users:", error);
        }
    }
    async getTotalProgressUsers() {
        try {
            const domain = [['status', '=', 'in_progress']]; // Define domain to filter records
            const totalClosedUsers = await this.orm.searchCount("support_sys.support_sys", domain);
            this.state.problem.progress = totalClosedUsers;
        } catch (error) {
            console.error("Error fetching total closed users:", error);
        }
    }
    async getFreshNewUsers() {
        try {
            const domain = [['status', '=', 'new']]; // Define domain to filter records
            const totalClosedUsers = await this.orm.searchCount("support_sys.support_sys", domain);
            this.state.problem.fresh = totalClosedUsers;
        } catch (error) {
            console.error("Error fetching total closed users:", error);
        }
    }
}

OwlReportingDashboard.template = "owl.OwlReportingDashboard";
OwlReportingDashboard.components = { KpiCard, ChartRenderer,CustomerCard};

registry.category('actions').add('dashboard.owl.new.registry', OwlReportingDashboard);