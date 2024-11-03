import './App.css'
import AboutMe from './components/AboutMe'
import CoverPhoto from './components/CoverPhoto'
import Education from './components/Education'
import JobHistory from './components/JobHistory'
import LinkedInProfile from './components/LinkedInProfile'
import ProfileHeader from './components/ProfileHeader'
import ProfileInfo from './components/ProfileInfo'
import ProfilePhoto from './components/ProfilePhoto'

export default function App() {
  return (
    <>
      <h1 className="text-3xl font-bold underline">
        Hello world!
      </h1>
      <LinkedInProfile>
      <CoverPhoto />
      <ProfileHeader>
        <ProfilePhoto />
        <ProfileInfo />
      </ProfileHeader>
      <AboutMe />
      <JobHistory />
      <Education />
      {/* Add more sections as needed */}
    </LinkedInProfile>
  </>
  )
}
