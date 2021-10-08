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
      h-64
      flex
      items-center
      justify-center
    "
  >
    <h1 class="text-4xl">{{ title }}</h1>
  </header>
</template>
