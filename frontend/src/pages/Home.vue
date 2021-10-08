<script lang="ts">
import { defineComponent } from 'vue'
import Hero from '../components/Hero.vue'
import Section from '../components/Section.vue'
import Form from '../components/Form.vue'

export default defineComponent({
  setup() {},
  components: {
    Hero,
    Section,
    Form,
  },
})
</script>


<template>
  <Hero title="Do you have what it takes to be a Maverick?"></Hero>
  <Section>
    <Form></Form>
  </Section>
</template>

<style>
</style>