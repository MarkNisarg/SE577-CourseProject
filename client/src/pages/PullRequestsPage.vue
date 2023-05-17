<template>
  <h1>Pull Requests using GitHub REST API</h1>
  <div v-if="allPrsData.length > 0">
    <div class="form-wrap">
      <select v-model="queryValue">
        <option value="">All Repositories</option>
        <option v-for="(repo, roWNum) in repos" :key="roWNum">{{ repo }}</option>
      </select>
      <button class="button" type="button" @click="fetchPullRequestsInfo()">
        <span>Get Pull Requests</span></button>
    </div>

    <div class="repo-pulls-wrap" v-for="pr in prData" :key="pr.id">
      <div class="pull-wrap">
        <div class="link-wrap">
          <a :href="pr.html_url" target="_blank" rel="noopener"> {{ pr.title }} </a>
          <p> By {{ pr.user.login }}</p>
        </div>
        <p> {{ pr.state }} </p>
        <p class="repo-wrap"> Repository: {{ pr.head.repo.name }}</p>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
  export default {
    name: 'PullRequestPage'
  };
</script>

<script setup lang='ts'>
  import { onMounted, ref } from 'vue';
  import type { RepositoryApiInterface, ApiErrorInterface } from './ApiInterfaces';
  import axios, { AxiosError } from 'axios';

  const queryValue = ref('');
  const apiErrorInfo = ref<ApiErrorInterface>({ isError: false, errorCode: 0, errorMessage: '' })

  let allPrsData = ref<RepositoryApiInterface[]>([]);
  let prData = ref<RepositoryApiInterface[]>([]);
  let repos: any[] = []

  let apiPrefix = 'http://localhost:9095/pulls'

  // Fetch pull requests for given query on button click.
  const fetchPullRequestsInfo = async () => {
    let apiEndPoint = queryValue.value ? '/' + queryValue.value : ''
    let apiURL = apiPrefix + apiEndPoint

    try {
      let repositoryAPI = await axios.get<RepositoryApiInterface[]>(apiURL)

      if (repositoryAPI.status == 200) {
        apiErrorInfo.value.isError = false;
        apiErrorInfo.value.errorCode = repositoryAPI.status;
        apiErrorInfo.value.errorMessage = repositoryAPI.statusText;
        prData.value = repositoryAPI.data
      } else {
        console.log('Something is wrong!')
      }
    } catch (err) {
      let e = err as AxiosError
      if (e.response) {
        apiErrorInfo.value.isError = true;
        apiErrorInfo.value.errorCode = e.response.status;
        apiErrorInfo.value.errorMessage = e.request.statusText;
        console.log('Got Error Code: ', e.response.status)
      }
    }
  }

  // Get all pull requests from all repos on mount.
  onMounted(async () => {
    let repositoryAPI = await axios.get<RepositoryApiInterface[]>(apiPrefix)
    // If OK, get all data.
    if (repositoryAPI.status == 200) {
      prData.value = allPrsData.value = repositoryAPI.data
      allPrsData.value.forEach(pr => {
        if (!repos.includes(pr.head.repo.name)) {
          repos.push(pr.head.repo.name)
        }
      });
    }
  });

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.form-wrap {
  margin: 50px 0;
  text-align: center;
}

.pull-wrap {
  border: 1px solid var(--vt-c-indigo);
  border-radius: 3px;
  padding: 10px;
  margin-bottom: 15px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  flex-wrap: nowrap;
  font-family: monospace;
  font-size: 16px;
  background: var(--vt-c-white-softer);
}

.pull-wrap .link-wrap {
  flex: 0 0 50%;
}

.pull-wrap .link-wrap a {
  font-size: 22px;
  color: var(--vt-c-indigo);
  font-weight: bold;
}

.pull-wrap .link-wrap p {
  color: var(--vt-c-gray);
  margin: 0;
}

.pull-wrap .link-wrap a:hover,
.pull-wrap .link-wrap a:focus {
  background-color: transparent;
  text-decoration: underline;
}

.pull-wrap .repo-wrap {
  flex: 0 0 33%;
  text-align: right;
}

select {
  font-size: 18px;
  font-family: monospace;
  padding: 8px;
  background: var(--vt-c-white-softer);
}

.button {
  display: inline-block;
  border-radius: 4px;
  background-color: var(--vt-c-indigo);
  border: none;
  color: var(--vt-c-white);
  text-align: center;
  font-size: 20px;
  padding: 8px 20px;
  transition: all 0.5s;
  cursor: pointer;
  font-family: monospace;
  margin-left: 50px;
}

.button span {
  cursor: pointer;
  display: inline-block;
  position: relative;
  transition: 0.5s;
}

.button span:after {
  content: '\00bb';
  position: absolute;
  opacity: 0;
  top: 0;
  right: -20px;
  transition: 0.5s;
}

.button:hover span {
  padding-right: 25px;
}

.button:hover span:after {
  opacity: 1;
  right: 0;
}
</style>
