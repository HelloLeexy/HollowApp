<template>

  <div class="contact-us">
    <div class="header">
      <div class="image-container">
        <img src="@/assets/images/banner.png" alt="banner" style="width:100%; height:auto;" />
        <div class="overlay">
          <h1>{{ title }}</h1>
          <p>{{ content }}</p>
        </div>
      </div>
    </div>
    <div class="footer">
      <p>Contact us at: group30@gla.ac.uk<br>
      Address: University of Glasgow, Glasgow, UK, G12 8QQ</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: 'We would love to hearing from you!',
      content: 'Please contact us if you have any question.'
    };
  }
};
</script>

<style>
.contact-us {
  text-align: center;
}

.header {
  position: relative;
}

.image-container {
  position: relative;
  display: inline-block;
}

.overlay {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  color: black;
}

.overlay h1 {
  font-size: 2em;
  margin: 10px 0;
  white-space: nowrap;
}

.overlay p {
  font-size: 1em;
  margin: 10px 0;
  white-space: nowrap;
}

.footer {
  background-color: #f0f0f0;
  padding: 10px;
  display: flex; 
  justify-content: center; 
  align-items: flex-end; 
}
</style>