<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  setup() {},
  props: ['title'],
})
</script>

<template>
  <header
    class="
      bg-gray-700
      text-white
      p-16
      text-center
      flex
      items-center
      justify-center
    "
  >
    <h1 class="text-4xl">{{ title }}</h1>
  </header>
</template>

<style scoped>
header {
  min-height: 50vh;
}
h1 {
  font-size: 75px;
  line-height: 1;
}
</style>