<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <div class="navigation-wrapper">
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/repositories">Repositories</RouterLink>
        <RouterLink to="/pulls">Pull Requests</RouterLink>
      </nav>
    </div>
  </header>

  <div class="main-content">
    <RouterView />
  </div>
</template>

<style scoped>
  header {
    line-height: 1.5;
    max-height: 100vh;
  }

  .logo {
    display: block;
    margin: 0 auto 2rem;
  }

  nav {
    width: 100%;
    font-size: 12px;
    text-align: center;
    padding: 18px;
    font-size: 22px;
    position: relative;
    box-shadow: 0 0 9px 0 rgb(0 0 0 / 50%);
  }

  nav a.router-link-exact-active {
    color: var(--vt-c-black);
    background-color: var(--vt-c-active-link);
  }

  nav a.router-link-exact-active:hover {
    background-color: var(--vt-c-active-link);
  }

  nav a {
    display: inline-block;
    padding: 4px 25px 6px;
    border-left: 1px solid var(--color-border);
    border-radius: 3px;
  }

  nav a:first-of-type {
    border: 0;
  }

  .main-content {
    padding: 20px;
    max-width: 1180px;
    margin: 0 auto;
  }
</style>
