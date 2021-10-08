<script lang="ts">
import { defineComponent } from 'vue'
import Hero from '../components/Hero.vue'
import Section from '../components/Section.vue'

export default defineComponent({
  setup() {},
  components: {
    Hero,
    Section,
  },
})
</script>


<template>
  <Hero title="About"></Hero>
  <Section><h2 class="text-center">This could be an about page.</h2></Section>
</template>
