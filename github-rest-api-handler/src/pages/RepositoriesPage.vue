<template>
  <h1>My GitHub Repositories</h1>
  <p>
    Welcome to my GitHub repositories page! Here you can find all of the public repositories that I have created and contributed to on GitHub. From open-source projects to personal experiments, this page provides a comprehensive overview of my coding journey.
  </p>
  <p>
    Each repository on this page contains a wealth of information about the project, including the description, the programming language used, and the date it was last updated. You can also browse through the repository's files, fork the repository to create your own copy, and even submit issues or pull requests if you have suggestions or contributions to make.
  </p>
  <p>
    So take a look around and see what catches your eye and if you have any questions or feedback, don't hesitate to reach out and let me know!
  </p>

  <h2>List Repositories:</h2>
  <p>All repositories will be listed here using GitHub REST API Request...</p>

  <table>
    <tr>
      <th>Name</th>
      <th>URL</th>
      <th>Description</th>
      <th>Contributors</th>
      <th>Languages</th>
    </tr>
    <tr>
      <td>Vaccination</td>
      <td><a href="https://github.com/MarkNisarg/Vaccination" target="_blank" rel="noopener">Open in GitHub</a></td>
      <td>Vaccine Reminder & Vaccine Schedule</td>
      <td>MarkNisarg, geeta-kukreja, Lavan-ya</td>
      <td>HTML, CSS, JavaScript, Python</td>
    </tr>
    <tr>
      <td>SE577-CourseProject</td>
      <td><a href="https://github.com/MarkNisarg/SE577-CourseProject" target="_blank" rel="noopener">Open in GitHub</a></td>
      <td>Software Architecture</td>
      <td>MarkNisarg</td>
      <td>HTML, CSS, TypeScript, Vue</td>
    </tr>
  </table>
</template>

<script lang="ts">
  export default {
    name: 'ProjectPage',
  };
</script>

<script setup lang="ts">
   // Most code goes here.
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  table {
    border: 1px solid var(--vt-c-indigo);
    border-collapse: collapse;
    margin: 25px 0;
    font-size: 18px;
  }

  th, td {
    padding: 10px;
    border: 1px solid var(--vt-c-indigo);
  }

  th {
    font-weight: bold;
    background-color: var(--vt-c-active-link);
  }

  td a {
    color: #043963;
    text-decoration: underline;
  }

  td a:hover,
  td a:focus {
    background-color: transparent;
    text-decoration: underline;
  }
</style>
