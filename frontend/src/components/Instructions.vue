<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue'
import { getInstructions as getInstructionsFromAPI } from '../api'
import { wait } from '../util'

type InstructionsResponse = {
  content: string
}

export default defineComponent({
  setup() {
    const isLoading = ref(true)
    const instructions = ref('')
    const testAssignment =
      location.pathname !== '/'
        ? location.pathname.substring(1)
        : location.pathname

    const getInstructions = async () => {
      await wait(1000)
      const json: InstructionsResponse = await getInstructionsFromAPI(
        testAssignment
      )
      instructions.value = json.content
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
  <div v-else v-html="instructions" class="instructions"></div>
</template>

<style>
.instructions p,
.instructions ol {
  @apply mb-4 list-inside;
}
.instructions ol ul {
  @apply ml-4 mb-2 list-inside;
}
.instructions ol li {
  @apply list-decimal;
}
.instructions ol ul li {
  @apply list-disc;
}
.instructions table {
  @apply table-auto;
}
.instructions td {
  @apply border-2 p-2;
}
</style>