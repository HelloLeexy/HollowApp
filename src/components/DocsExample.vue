<template src="./DocsExample.html" >

</template>

<script>
export default {
  name: 'DocsExample',
  props: {
    href: String,
    tabContentClass: String,
  },
  setup(props) {
    const url = `https://coreui.io/vue/docs/${props.href}`
    const addClass = props.tabContentClass
 
    return {
      addClass,
      url,
    }
  },
}
</script>
