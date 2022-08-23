#!/bin/bash
#
# Copyright (c) 2020, 2022 Red Hat, IBM Corporation and others.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
##### Script for validating HPO (Hyper Parameter Optimization) /experiment_trials API #####

# Generate the curl command based on the test name passed and get the result by querying it.
# input: Test name and Trial number
function run_get_plot_test() {
	exp_trial=$1
	plot_type=$2

	curl="curl -H 'Accept: application/json'"
	url="http://${SERVER_IP}:${PORT}/plot"
	echo "url = $url"

	case "${exp_trial}" in
		empty-name)
			get_plot=$(${curl} ''${url}'?experiment_name=%20&type=tunables_importance' -w '\n%{http_code}' 2>&1)
			get_plot_cmd="${curl} '${url}?experiment_name=%20&type=tunables_importance' -w '\n%{http_code}'"
			;;
		no-name)
			get_plot=$(${curl} ''${url}'?&type=tunables_importance' -w '\n%{http_code}' 2>&1)
			get_plot_cmd="${curl} '${url}?&type=tunables_importance' -w '\n%{http_code}'"
			;;
		null-name)
			get_plot=$(${curl} ''${url}'?experiment_name=null&type=tunables_importance' -w '\n%{http_code}' 2>&1)
			get_plot_cmd="${curl} '${url}?experiment_name=null&type=tunables_importance' -w '\n%{http_code}'"
			;;
		only-valid-name)
			get_plot=$(${curl} ''${url}'?experiment_name='${current_name}'' -w '\n%{http_code}' 2>&1)
			get_plot_cmd="${curl} '${url}?experiment_name='${current_name}'' -w '\n%{http_code}'"
			;;
		invalid-type)
			get_plot=$(${curl} ''${url}'?experiment_id='${current_name}'&type=102yrt' -w '\n%{http_code}' 2>&1)
			get_plot_cmd="${curl} '${url}?experiment_id='${current_name}'&type=102yrt' -w '\n%{http_code}'"
			;;
		empty-type)
			get_plot=$(${curl} ''${url}'?experiment_id='${current_name}'&type=' -w '\n%{http_code}' 2>&1)
			get_plot_cmd="${curl} '${url}?experiment_id='${current_name}'&type=' -w '\n%{http_code}'"
			;;
		no-type)
			get_plot=$(${curl} ''${url}'?experiment_id='${current_name}'' -w '\n%{http_code}' 2>&1)
			get_plot_cmd="${curl} '${url}?experiment_id='${current_name}'' -w '\n%{http_code}'"
			;;
		null-type)
			get_plot=$(${curl} ''${url}'?experiment_id='${current_name}'&type=null' -w '\n%{http_code}' 2>&1)
			get_plot_cmd="${curl} '${url}?experiment_id='${current_name}'&type=null' -w '\n%{http_code}'"
			;;
		only-valid-type)
			get_plot=$(${curl} ''${url}'?type=optimization_history' -w '\n%{http_code}' 2>&1)
			get_plot_cmd="${curl} '${url}?type=optimization_history' -w '\n%{http_code}'"
			;;
		valid-exp-type)
			get_plot=$(${curl} ''${url}'?experiment_name=petclinic-sample-2-75884c5549-npvgd&type='${plot_type}'' -w '\n%{http_code}' 2>&1)
			get_plot_cmd="${curl} '${url}?experiment_name=petclinic-sample-2-75884c5549-npvgd&type=${plot_type}' -w '\n%{http_code}'"
			;;
	esac

	echo "command used to query the plot API = ${get_plot_cmd}" | tee -a ${LOG_} ${LOG}
	echo "" | tee -a ${LOG_} ${LOG}
	echo "${get_plot}" >> ${LOG_} ${LOG}
	http_code=$(tail -n1 <<< "${get_plot}")
	response=$(echo -e "${get_plot}" | tail -2 | head -1)
	response=$(echo ${response} | cut -c 4-)
	echo "${response}" > ${result}
}


# validate obtaining plot from HPO /plot API for invalid queries
# input: test name 
function get_plot_invalid_tests() {
	__test_name__=$1

	SERV_LOG="${TEST_DIR}/service.log"

	# Deploy hpo
	if [ ${cluster_type} == "native" ]; then
		deploy_hpo ${cluster_type} ${SERV_LOG}
	else
		deploy_hpo ${cluster_type} ${HPO_CONTAINER_IMAGE} ${SERV_LOG}
	fi
	
	# Check if HPO services are started
	check_server_status "${SERV_LOG}"

	IFS=' ' read -r -a get_plot_invalid_tests <<<  ${hpo_get_plot_tests[$FUNCNAME]}
	for exp_trial in "${get_plot_invalid_tests[@]}"
	do
		# Get the length of the service log before the test
		log_length_before_test=$(cat ${SERV_LOG} | wc -l)

		TESTS_="${TEST_DIR}/${exp_trial}"
		mkdir -p ${TESTS_}
		LOG_="${TEST_DIR}/${exp_trial}.log"
		result="${TESTS_}/${exp_trial}_result.log"

		TEST_SERV_LOG="${TESTS_}/service.log"

		echo "************************************* ${exp_trial} Test ****************************************" | tee -a ${LOG_} ${LOG}

		# Get the experiment id from search space JSON
		exp="valid-experiment"
		current_id=$(echo ${hpo_post_experiment_json[${exp}]} | jq '.search_space.experiment_id')
		current_name=$(echo ${hpo_post_experiment_json[${exp}]} | jq '.search_space.experiment_name')

		# Post a valid experiment to HPO /experiment_trials API.
		post_experiment_json "${hpo_post_experiment_json[$exp]}"

		# Run the get plot API test
		run_get_plot_test ${exp_trial}

		# Extract the lines from the service log after log_length_before_test
		extract_lines=`expr ${log_length_before_test} + 1`
		cat ${SERV_LOG} | tail -n +${extract_lines} > ${TEST_SERV_LOG}
		
		echo ""
		echo "log_length_before_test ${log_length_before_test}"
		echo "extract_lines ${extract_lines}"
		echo ""

		actual_result="${http_code}"

		expected_result_="400"

		expected_log_msg="${hpo_get_plot_msgs[$exp_trial]}"

		echo "actual_result = $actual_result expected_result = $expected_result_"
		compare_result ${exp_trial} ${expected_result_} "${expected_log_msg}" "${TEST_SERV_LOG}"
		echo ""
		
		stop_experiment "$current_name"
	done
	
	# Stop the HPO servers
	echo "Terminating any running HPO servers..." | tee -a ${LOG_} ${LOG}
	terminate_hpo ${cluster_type} | tee -a ${LOG_} ${LOG}
	echo "Terminating any running HPO servers...Done" | tee -a ${LOG_} ${LOG}
	
	# Sleep for few seconds to reduce the ambiguity
	sleep 5
	echo "*********************************************************************************************************" | tee -a ${LOG_} ${LOG}
}

# Post a valid experiment to HPO /experiment_trials API, Query it using valid experiment id and trial number and validate the plot API
# input: test name
function get_plot_valid_tests() {
	__test_name__=$1

	SERV_LOG="${TEST_DIR}/service.log"
	# Deploy hpo
	if [ ${cluster_type} == "native" ]; then
		deploy_hpo ${cluster_type} ${SERV_LOG}
	else
		deploy_hpo ${cluster_type} ${HPO_CONTAINER_IMAGE} ${SERV_LOG}
	fi
	
	# Check if HPO services are started
	check_server_status "${SERV_LOG}"

	IFS=' ' read -r -a get_plot_valid_tests <<<  ${hpo_get_plot_tests[$FUNCNAME]}
	for experiment_trial in "${get_plot_valid_tests[@]}"
	do
		TESTS_="${TEST_DIR}/${FUNCNAME}"
		mkdir -p ${TESTS_}
		LOG_="${TEST_DIR}/${FUNCNAME}.log"
		result="${TESTS_}/${experiment_trial}_result.log"
		expected_json="${TESTS_}/${experiment_trial}_expected_json.json"
		TEST_SERV_LOG="${TESTS_}/${experiment_trial}_service.log"

		echo "************************************* ${experiment_trial} Test ****************************************" | tee -a ${LOG_} ${LOG}

		# Get the length of the service log before the test
		log_length_before_test=$(cat ${SERV_LOG} | wc -l)

		# Get the experiment id from search space JSON
		exp="valid-experiment"
		current_id=$(echo ${hpo_post_experiment_json[${exp}]} | jq '.search_space.experiment_id')
		current_name=$(echo ${hpo_post_experiment_json[${exp}]} | jq '.search_space.experiment_name')

		N_TRIALS=5
		expected_http_code="200"
	
		## Loop through the trials
		for (( i=0 ; i<${N_TRIALS} ; i++ ))
		do
			echo ""
			echo "*********************************** Trial ${i} *************************************"
			LOG_="${TEST_DIR}/hpo-trial-${i}.log"
			if [ ${i} == 0 ]; then
				# Post the experiment
				echo "Start a new experiment with the search space json..." | tee -a ${LOG}
				post_experiment_json "${hpo_post_experiment_json["valid-experiment"]}"
				verify_result "Post new experiment" "${http_code}" "${expected_http_code}"
			fi

			# Get the config from HPO
			echo ""
			echo "Generate the config for trial ${i}..." | tee -a ${LOG}
			echo ""

			curl="curl -H 'Accept: application/json'"
			hpo_url="http://${SERVER_IP}:${PORT}/experiment_trials"

			get_trial_json=$(${curl} ''${hpo_url}'?experiment_name=petclinic-sample-2-75884c5549-npvgd&trial_number='${i}'' -w '\n%{http_code}' 2>&1)

			get_trial_json_cmd="${curl} ${hpo_url}?experiment_name="petclinic-sample-2-75884c5549-npvgd"&trial_number=${i} -w '\n%{http_code}'"
			echo "command used to query the experiment_trial API = ${get_trial_json_cmd}" | tee -a ${LOG}

			# check for curl '000' error
			curl_error_check
	
			result="${TEST_DIR}/hpo_config_${i}.json"
			expected_json="${TEST_DIR}/expected_hpo_config_${i}.json"

			echo "${response}" > ${result}
			cat $result
			verify_result "Get config from hpo trial ${i}" "${http_code}" "${expected_http_code}"

			# Post the experiment result to hpo
			echo "" | tee -a ${LOG}
			echo "Post the experiment result for trial ${i}..." | tee -a ${LOG}
			trial_result="success"
			result_value="98.7"
			exp_result_json='{"experiment_name":'${exp_name}',"trial_number":'${i}',"trial_result":"'${trial_result}'","result_value_type":"double","result_value":'${result_value}',"operation":"EXP_TRIAL_RESULT"}'
			post_experiment_result_json ${exp_result_json}
			verify_result "Post experiment result for trial ${i}" "${http_code}" "${expected_http_code}"

			# Generate a subsequent trial
			if [[ ${i} < $((N_TRIALS-1)) ]]; then
				echo "" | tee -a ${LOG}
				echo "Generate subsequent config after trial ${i} ..." | tee -a ${LOG}
				subsequent_trial='{"experiment_name":'${exp_name}',"operation":"EXP_TRIAL_GENERATE_SUBSEQUENT"}'
				post_experiment_json ${subsequent_trial}
				verify_result "Post subsequent experiment after trial ${i}" "${http_code}" "${expected_http_code}"
			fi
		done


		# Query the HPO /plot API for valid experiment id and plot type
		type="parallel_coordinate"
		run_get_plot_test "valid-exp-type" "${type}"

		# Extract the lines from the service log after log_length_before_test
		extract_lines=`expr ${log_length_before_test} + 1`
		cat ${SERV_LOG} | tail -n +${extract_lines} > ${TEST_SERV_LOG}
		
		echo ""
		echo "log_length_before_test ${log_length_before_test}"
		echo "extract_lines ${extract_lines}"
		echo ""

		actual_result="${http_code}"

		expected_result_="200"
		expected_behaviour="Trial_Number = 0"
	
		compare_result ${experiment_trial} ${expected_result_} "${expected_behaviour}" "${TEST_SERV_LOG}"

		if [[ ${failed} -eq 1 ]]; then
			FAILED_CASES+=(${experiment_trial})
		fi

		stop_experiment "$current_name"

		echo "*********************************************************************************************************" | tee -a ${LOG_} ${LOG}
	done

	# Stop the HPO servers
	echo "Terminating any running HPO servers..." | tee -a ${LOG_} ${LOG}
	terminate_hpo ${cluster_type} | tee -a ${LOG_} ${LOG}
	echo "Terminating any running HPO servers...Done" | tee -a ${LOG_} ${LOG}
	
	# Sleep for few seconds to reduce the ambiguity
	sleep 5
}

# Tests for HPO GET PLOT API
function hpo_get_plot_test(){
	for test in "${!hpo_get_plot_tests[@]}"
	do
		${test} "${FUNCNAME}"
	done 
}

