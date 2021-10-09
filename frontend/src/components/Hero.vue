<script lang="ts">
import { defineComponent, onMounted } from 'vue'

export default defineComponent({
  setup() {
    // Circumvent Chrome not looping video correctly
    const loop = () => {
      const video = document.getElementsByTagName('video')[0]
      video.onended = () => {
        video.load()
        video.play()
      }
    }
    onMounted(loop)
  },
  props: ['title'],
  methods: {},
})
</script>

<template>
  <header
    class="
      relative
      bg-gray-700
      text-white
      p-16
      text-center
      flex
      items-center
      justify-center
    "
  >
    <video src="/assets/mathlady.mp4" autoplay muted loop class="video"></video>
    <h1 class="text-4xl">{{ title }}</h1>
  </header>
</template>

<style scoped>
header {
  min-height: 600px;
  max-width: 1280px;
}
h1 {
  font-size: 75px;
  line-height: 1;
  position: relative;
  z-index: 1;
}
.video {
  position: absolute;
  right: 0;
  bottom: 0;
  min-width: 100%;
  min-height: 100%;
  z-index: 0;
}
@media screen and (max-width: 1024px) {
  .video {
    display: none;
  }
}
</style>