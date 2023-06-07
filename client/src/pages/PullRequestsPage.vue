<template>
  <h1>Pull Requests using GitHub REST API</h1>
  <div v-if="allPrsData.length > 0">
    <div class="form-wrap">
      <select v-model="selectedRepo">
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
          <p> To merge changes from <b>{{ pr.head.ref }}</b> to <b>{{ pr.base.ref }}</b></p>
        </div>
        <p> {{ pr.state }} </p>
        <p class="repo-wrap"> Repository: {{ pr.head.repo.name }}</p>
        <div class="btn-grp">
          <button @click="postComment(pr.head.repo.name, pr.number)" class="button comment-btn">
            Leave Comment
          </button>
          <button @click="mergePullRequest(pr.head.repo.name, pr.number)" class="button marge-btn">
            Merge Pull Request
          </button>
          <button @click="closePullRequest(pr.head.repo.name, pr.number)" class="button close-btn">
            Close Pull Request
          </button>
        </div>
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
  import type { PullRequestsApiInterface, ApiErrorInterface } from './ApiInterfaces';
  import axios, { AxiosError } from 'axios';

  const selectedRepo = ref('');
  const apiErrorInfo = ref<ApiErrorInterface>({ isError: false, errorCode: 0, errorMessage: '' })

  let allPrsData = ref<PullRequestsApiInterface[]>([]);
  let prData = ref<PullRequestsApiInterface[]>([]);
  let repos: any[] = []

  let apiPrefix = 'http://localhost:9095/pulls'

  // Fetch pull requests for given query on button click.
  const fetchPullRequestsInfo = async () => {
    let apiEndPoint = selectedRepo.value ? '/' + selectedRepo.value : ''
    let apiURL = apiPrefix + apiEndPoint

    try {
      let pullRequestsAPI = await axios.get<PullRequestsApiInterface[]>(apiURL)

      if (pullRequestsAPI.status == 200) {
        apiErrorInfo.value.isError = false;
        apiErrorInfo.value.errorCode = pullRequestsAPI.status;
        apiErrorInfo.value.errorMessage = pullRequestsAPI.statusText;
        prData.value = pullRequestsAPI.data
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

  // Post comment on pull request.
  const postComment = async (repoName: string, pullNumber: number) => {
    let apiEndPoint = `/${repoName}/comment`;
    let apiURL = apiPrefix + apiEndPoint;

    const comment = prompt('Enter your comment to PR:');

    if (comment) {
      try {
        const response = await axios.post<PullRequestsApiInterface[]>(apiURL, {
          pull_number: pullNumber,
          comment: comment,
        });
        fetchPullRequestsInfo();
        alert(response.data);
      }
      catch (error) {
        console.error(error);
        alert('Failed to post comment!');
      }
    }
  }

  // Merge pull request.
  const mergePullRequest = async (repoName: string, pullNumber: number) => {
    let apiEndPoint = `/${repoName}/merge`;
    let apiURL = apiPrefix + apiEndPoint;

    try {
      const response = await axios.put<PullRequestsApiInterface[]>(apiURL, {
        pull_number: pullNumber
      });
      fetchPullRequestsInfo();
      alert(response.data);
    }
    catch (error) {
      console.error(error);
      alert('Failed to merge pull request!');
    }
  }

  // Close pull request.
  const closePullRequest = async (repoName: string, pullNumber: number) => {
    let apiEndPoint = `/${repoName}/close`;
    let apiURL = apiPrefix + apiEndPoint;

    try {
      const response = await axios.patch<PullRequestsApiInterface[]>(apiURL, {
        pull_number: pullNumber
      });
      fetchPullRequestsInfo();
      alert(response.data);
    }
    catch (error) {
      console.error(error);
      alert('Failed to merge pull request!');
    }
  }

  // Get all pull requests from all repos on mount.
  onMounted(async () => {
    let pullRequestsAPI = await axios.get<PullRequestsApiInterface[]>(apiPrefix)
    // If OK, get all data.
    if (pullRequestsAPI.status == 200) {
      prData.value = allPrsData.value = pullRequestsAPI.data
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
  flex-wrap: wrap;
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

.btn-grp {
  flex-basis: 100%;
  margin: 15px auto 5px;
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  align-items: center;
}

.comment-btn,
.marge-btn,
.close-btn {
  margin-left: 0;
  font-size: 20px;
}

.comment-btn {
  background-color: var(--vt-c-comment-btn);
  color: var(--vt-c-black);
}

.marge-btn {
  background-color: var(--vt-c-merge-btn);
}

.close-btn {
  background-color: var(--vt-c-close-btn);
}
</style>
