import json
from datetime import datetime

zabbix_alert = {
    "host": "DB-01",
    "trigger": "Disk space is critically low (95%)",
    "severity": "High",
    "timestamp": datetime.now().isoformat()
}

def determine_priority(severity):
    if severity == "Disaster": return "P1"
    elif severity == "High": return "P2"
    elif severity == "Average": return "P3"
    else: return "P4"

def create_itsm_ticket(alert):
    priority = determine_priority(alert['severity'])
    ticket_payload = {
        "project": "MONITORING",
        "summary": f"[{priority}] Alert on {alert['host']}: {alert['trigger']}",
        "description": f"Сервер: {alert['host']}\nПроблема: {alert['trigger']}",
        "priority": priority
    }
    print("--- Отправка тикета в ITSM ---")
    print(json.dumps(ticket_payload, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    create_itsm_ticket(zabbix_alert)
