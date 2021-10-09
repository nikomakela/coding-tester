<script lang="ts">
import { defineComponent } from 'vue'
import Hero from '../components/Hero.vue'
import Section from '../components/Section.vue'
import Instructions from '../components/Instructions.vue'
import Form from '../components/Form.vue'

export default defineComponent({
  setup() {},
  components: {
    Hero,
    Section,
    Instructions,
    Form,
  },
})
</script>


<template>
  <Hero title="Do you have what it takes to be a Maverick?"></Hero>
  <Section class="bg-gray-800">
    <Instructions />
  </Section>
  <Section class="bg-gray-900">
    <Form />
  </Section>
</template>
