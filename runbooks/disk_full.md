# 🚨 Runbook: Переполнение диска (Disk Full)

**Триггер:** Алерт из Zabbix: `Free disk space is less than 10% on /`.
**Приоритет:** P1 (Критический).
**SLA:** 15 минут.

## 1. Диагностика
1. Подключиться по SSH: `ssh user@<IP>`
2. Проверить разделы: `df -h`
3. Найти тяжелые папки: `sudo du -sh /* 2>/dev/null | sort -hr | head -n 10`
4. Найти большие логи: `sudo find /var/log -type f -size +100M -exec ls -lh {} \;`

## 2. Решение
1. Очистить логи: `sudo truncate -s 0 /var/log/<имя_файла>.log`
2. Очистить кэш: `sudo apt clean`

## 3. Проверка
1. `df -h` (должно быть > 15% свободно).
2. Закрыть тикет в ITSM.
