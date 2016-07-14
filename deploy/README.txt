to backup db:
(manually: sudo -u root sudo -u postgres pg_dump -Fc %s > %s )
import: sudo -u root sudo -u postgres pg_restore -c -d satch < prodJan27.db