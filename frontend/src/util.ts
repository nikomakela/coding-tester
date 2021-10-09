// For simulating network lag
export const wait = async (ms: number) => {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(true)
    }, ms)
  })
}

export const getAssignmentName = () =>
  location.pathname !== '/' ? location.pathname.substring(1) : 'fibonacci' // <-- DEFAULT ASSIGNMENT
