<template>
  <CSidebar class="custom-background" colorScheme="light" position="fixed">
    <div class="sidebar-header">UofG Tree Hole</div>
    <router-link to="/dashboard" class="router-link">Home</router-link>
    <router-link to="/account" class="router-link">My Account</router-link>
    <router-link to="/follow" class="router-link">Follow</router-link>
    <router-link to="/post" class="router-link">Post</router-link>
    <router-link to="/contact" class="router-link">Contact us</router-link>
    <router-link to="/Login" class="router-link logout">Log out</router-link>
  </CSidebar>
</template>

<style>
.custom-background {
  background: url('@/assets/images/building.png') no-repeat right center;
  background-size: cover;
  width: 250px;
}

.sidebar-header {
  padding: 1rem;
  font-size: 1.5rem;
  font-weight: bold; /* Make the text bold */
  text-align: center;
  padding-left: 30px;
  background-color: rgba(255, 255, 255, 0.5); /* Semi-transparent white background */
  color: #000; /* Black text */
  border-bottom: 0px solid #e7e7e7; /* Light grey border */
}

.router-link {
  display: block;
  font-size: large;
  padding: 0.75rem 1rem;
  color: #000; /* Black text */
  background-color: rgba(255, 255, 255, 0.5); /* Semi-transparent white background */
  border: 1px solid #fff; /* White border */
  text-decoration: none;
  margin: 0;
  text-align: center;
  transition: background-color 0.2s ease-in-out;
}

.router-link:not(.logout):hover {
  background-color: #808080; /* Light grey background on hover */
  color: #000; /* Black text */
}

.logout {
  color: #000; /* Black text for logout */
  text-align: center;
}

.logout:hover {
  color: #fff; /* White text */
  background-color: #d9534f; /* Red background */
}
</style>

<script>
export default {
  // component options
}
</script>
