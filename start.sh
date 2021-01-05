#!/usr/bin/env bash

kill $(ps aux | grep '3263' | awk '{print $2}')  > /dev/null 2> /dev/null || :

if [[ -z "$FLASK_ENV" ]]; then
	echo "WARNING! FLASK_ENV not set, will use **DEV** by default."
fi

THREAD_COUNT=4
if [[ $FLASK_ENV == 'PROD-LEGACY' ]] || [[ $FLASK_ENV == 'PROD' ]]; then
	THREAD_COUNT=8
fi

echo "Environment: $FLASK_ENV"
echo "Thread Count: $THREAD_COUNT"

gunicorn -k gevent -w $THREAD_COUNT -b 0.0.0.0:3263 h5_portal:app -t 6000000 --daemon