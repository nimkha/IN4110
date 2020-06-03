#!/bin/bash

option=$1;
export LOGFILE="logfile.txt"

case "$option" in
-start)
    if [[ ! -e ${LOGFILE} ]]; then
        touch ${LOGFILE}
    fi

    last_line_first_word=$(cat ${LOGFILE} | tail -n 1 | awk '{print $1}');

    if [[ "$last_line_first_word" != "LABEL" || "$last_line_first_word" == "" ]]; then
        label=$2;
        start_value=$(LC_ALL=en_US.UTF-8 date);
        echo "START -> \"${start_value}\"" >> ${LOGFILE};
        echo "LABEL -> \"${label}\"" >> ${LOGFILE};

        else
            echo "Task already running. Close task before starting new";
    fi
;;
-stop)
    last_line_first_word=$(cat ${LOGFILE} | tail -n 1 | awk '{print $1}');

    if [[ "$last_line_first_word" == "LABEL" || "$last_line_first_word" == " " ]]; then

        stop_value=$(LC_ALL=en_US.UTF-8 date);
        echo "STOP -> \"${stop_value}\"" >> ${LOGFILE};

        start_value=$(cat ${LOGFILE} | grep "START" | tail -n 1 | cut -d"\"" -f2);
        start_time_in_seconds=$(date -d "$start_value" +%s);
        stop_time_in_seconds=$(date -d "$stop_value" +%s);
        time_spent_on_task=$(( $stop_time_in_seconds-$start_time_in_seconds ));
        seconds=0;
        minutes=0;
        hours=0;
        days=0;

        if [[ ${time_spent_on_task} -gt 59 ]]; then
            seconds=$(( $time_spent_on_task%60 ));
            time_spent_on_task=$(( $time_spent_on_task/60 ));

            if [[ ${time_spent_on_task} -gt 59 ]]; then
                minutes=$(( $time_spent_on_task%60 ));
                time_spent_on_task=$(( $time_spent_on_task/60 ));

                if [[ ${time_spent_on_task} -gt 23 ]]; then
                    hours=$(( $time_spent_on_task%24 ));
                    days=$(( $time_spent_on_task/24 ));

                    else
                        hours=${time_spent_on_task};
                fi

                else
                    minutes=${time_spent_on_task};
            fi

            else
                seconds=${time_spent_on_task};
        fi

        label_name=$(cat logfile.txt | grep "LABEL" | tail -n 1 | cut -d "\"" -f2);
        echo "Time spent on task ${label_name} -> ${days}:${hours}:${minutes}:${seconds}" >> ${LOGFILE}
        echo "" >> ${LOGFILE}

    else
        echo "No task running. Start task before closing";
    fi
;;
-status)
    last_line_first_word=$(cat ${LOGFILE} | tail -n 1 | awk '{print $1}');
    if [[ "${last_line_first_word}" == "LABEL" ]]; then
        cat ${LOGFILE} | grep "LABEL" | tail -n 1;
            else
                echo "No tasks running";
    fi
;;

-log)
    cat ${LOGFILE} | grep "Time";

;;
*)
    echo "Invalid argument. Valid arguments are -start, -stop and -status";
    ;;
esac

