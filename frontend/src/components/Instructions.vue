<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue'
import { getInstructions as getInstructionsFromAPI } from '../api'
import { wait } from '../util'

export default defineComponent({
  setup() {
    const isLoading = ref(true)
    const instructions = ref('')

    const getInstructions = async () => {
      await wait(1000)
      const json = await getInstructionsFromAPI()
      console.log(json)
      instructions.value = 'Jeejee'
      isLoading.value = false
    }

    onMounted(getInstructions)

    return {
      isLoading,
      instructions,
    }
  },
  methods: {},
})
</script>

<template>
  <h2>Instructions</h2>

  <p v-if="isLoading">Loading...</p>
  <div v-else v-html="instructions"></div>
</template>