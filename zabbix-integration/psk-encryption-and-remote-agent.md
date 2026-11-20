# Шифрование agent–server (TLS + PSK) и мониторинг внешнего хоста

## Обзор

Все проверки агентов на стенде идут в зашифрованном виде: применяется
TLS с предобщим ключом (PSK, TLS 1.3). Шифрование настроено в обе
стороны — и на входящие (passive checks), и на исходящие (active checks)
соединения агента. Соединения без шифрования запрещены.

## Состав стенда

Стенд поднимается через Docker Compose (`compose.yaml`):

| Сервис | Образ | Назначение |
|---|---|---|
| zabbix-server | zabbix/zabbix-server-mysql:alpine-8.0-latest | сервер мониторинга, порт 10051 |
| zabbix-web | zabbix/zabbix-web-nginx-mysql:alpine-8.0-latest | веб-интерфейс, порт 80 |
| mysql-server | mysql:8.0 | БД Zabbix |
| zabbix-agent | zabbix/zabbix-agent:alpine-8.0-latest | локальный агент (мониторит контейнер сервера) |

Дополнительно к стенду подключён агент на отдельной ВМ
**Ubuntu-Server (192.168.0.198)** с шаблоном *Linux by Zabbix agent*.

## Настройка PSK

### 1. Генерация ключа

Ключ сгенерирован криптостойким способом (256 бит, hex):

```bash
openssl rand -hex 32
