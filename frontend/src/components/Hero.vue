<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  setup() {},
  props: ['title'],
})
</script>

<template>
  <header>
    <h1>{{ title }}</h1>
  </header>
</template>
