<script setup>
import { RouterView } from 'vue-router'
</script>

<template>
  <RouterView :url="url" />
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      url: window.location.protocol + '//' + window.location.hostname + (window.location.port ? ':' + window.location.port + '/' : '/')
    }
  }
}
</script>

<style scoped>
</style>