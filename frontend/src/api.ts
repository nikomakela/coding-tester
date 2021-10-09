export const getInstructions = async () => {
  console.log('instruction', import.meta.env.VITE_API_ENDPOINT)
  const response = await fetch(
    `${import.meta.env.VITE_API_ENDPOINT}?format=json`
  )
  const json = await response.json()
  return json
}

export default {
  getInstructions,
}
