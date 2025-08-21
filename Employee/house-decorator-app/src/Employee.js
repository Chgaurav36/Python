import React, { useState } from 'react';
import './DecoratorApplication.css';

const DecoratorApplication = () => {
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    email: '',
    phone: '',
    address: '',
    experience: '',
    specialties: [],
    portfolio: '',
    availability: 'full-time',
    salaryExpectation: '',
    references: '',
    aboutYou: ''
  });

  const [submitted, setSubmitted] = useState(false);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    
    if (type === 'checkbox') {
      let updatedSpecialties = [...formData.specialties];
      if (checked) {
        updatedSpecialties.push(value);
      } else {
        updatedSpecialties = updatedSpecialties.filter(item => item !== value);
      }
      setFormData({...formData, specialties: updatedSpecialties});
    } else {
      setFormData({...formData, [name]: value});
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Form submitted:', formData);
    setSubmitted(true);
    // Here you would typically send the data to your backend
  };

  if (submitted) {
    return (
      <div className="thank-you-container">
        <div className="thank-you-card">
          <h2>Thank You for Your Application!</h2>
          <p>We've received your application for the House Decorator position.</p>
          <p>Our HR team will review your information and contact you within 5-7 business days.</p>
          <div className="company-logo">
            <span>Elegant Spaces</span>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="application-container">
      <div className="application-header">
        <div className="company-info">
          <h1>Elegant Spaces</h1>
          <p>Transforming houses into dream homes since 2010</p>
        </div>
        <div className="job-title">
          <h2>House Decorator Position</h2>
          <p>Full-time/Part-time • Competitive Salary • Benefits</p>
        </div>
      </div>

      <form onSubmit={handleSubmit} className="application-form">
        <div className="form-section personal-info">
          <h3>Personal Information</h3>
          <div className="form-row">
            <div className="form-group">
              <label htmlFor="firstName">First Name*</label>
              <input 
                type="text" 
                id="firstName" 
                name="firstName" 
                value={formData.firstName} 
                onChange={handleChange} 
                required 
              />
            </div>
            <div className="form-group">
              <label htmlFor="lastName">Last Name*</label>
              <input 
                type="text" 
                id="lastName" 
                name="lastName" 
                value={formData.lastName} 
                onChange={handleChange} 
                required 
              />
            </div>
          </div>

          <div className="form-row">
            <div className="form-group">
              <label htmlFor="email">Email*</label>
              <input 
                type="email" 
                id="email" 
                name="email" 
                value={formData.email} 
                onChange={handleChange} 
                required 
              />
            </div>
            <div className="form-group">
              <label htmlFor="phone">Phone*</label>
              <input 
                type="tel" 
                id="phone" 
                name="phone" 
                value={formData.phone} 
                onChange={handleChange} 
                required 
              />
            </div>
          </div>

          <div className="form-group">
            <label htmlFor="address">Address</label>
            <input 
              type="text" 
              id="address" 
              name="address" 
              value={formData.address} 
              onChange={handleChange} 
            />
          </div>
        </div>

        <div className="form-section professional-info">
          <h3>Professional Information</h3>
          <div className="form-group">
            <label htmlFor="experience">Years of Decorating Experience*</label>
            <select 
              id="experience" 
              name="experience" 
              value={formData.experience} 
              onChange={handleChange} 
              required
            >
              <option value="">Select</option>
              <option value="0-1">0-1 years</option>
              <option value="2-5">2-5 years</option>
              <option value="5-10">5-10 years</option>
              <option value="10+">10+ years</option>
            </select>
          </div>

          <div className="form-group">
            <label>Specialties (Select all that apply)*</label>
            <div className="checkbox-group">
              <label>
                <input 
                  type="checkbox" 
                  name="specialties" 
                  value="residential" 
                  checked={formData.specialties.includes('residential')} 
                  onChange={handleChange} 
                />
                Residential
              </label>
              <label>
                <input 
                  type="checkbox" 
                  name="specialties" 
                  value="commercial" 
                  checked={formData.specialties.includes('commercial')} 
                  onChange={handleChange} 
                />
                Commercial
              </label>
              <label>
                <input 
                  type="checkbox" 
                  name="specialties" 
                  value="space-planning" 
                  checked={formData.specialties.includes('space-planning')} 
                  onChange={handleChange} 
                />
                Space Planning
              </label>
              <label>
                <input 
                  type="checkbox" 
                  name="specialties" 
                  value="color-consultation" 
                  checked={formData.specialties.includes('color-consultation')} 
                  onChange={handleChange} 
                />
                Color Consultation
              </label>
              <label>
                <input 
                  type="checkbox" 
                  name="specialties" 
                  value="furniture-selection" 
                  checked={formData.specialties.includes('furniture-selection')} 
                  onChange={handleChange} 
                />
                Furniture Selection
              </label>
            </div>
          </div>

          <div className="form-group">
            <label htmlFor="portfolio">Portfolio Link (Website, Instagram, etc.)</label>
            <input 
              type="url" 
              id="portfolio" 
              name="portfolio" 
              value={formData.portfolio} 
              onChange={handleChange} 
              placeholder="https://"
            />
          </div>

          <div className="form-row">
            <div className="form-group">
              <label>Availability*</label>
              <div className="radio-group">
                <label>
                  <input 
                    type="radio" 
                    name="availability" 
                    value="full-time" 
                    checked={formData.availability === 'full-time'} 
                    onChange={handleChange} 
                    required 
                  />
                  Full-time
                </label>
                <label>
                  <input 
                    type="radio" 
                    name="availability" 
                    value="part-time" 
                    checked={formData.availability === 'part-time'} 
                    onChange={handleChange} 
                  />
                  Part-time
                </label>
                <label>
                  <input 
                    type="radio" 
                    name="availability" 
                    value="contract" 
                    checked={formData.availability === 'contract'} 
                    onChange={handleChange} 
                  />
                  Contract/Freelance
                </label>
              </div>
            </div>

            <div className="form-group">
              <label htmlFor="salaryExpectation">Salary Expectation (per hour or annual)</label>
              <input 
                type="text" 
                id="salaryExpectation" 
                name="salaryExpectation" 
                value={formData.salaryExpectation} 
                onChange={handleChange} 
                placeholder="Rs.900 - Rs.2000/Day"
              />
            </div>
          </div>
        </div>

        <div className="form-section additional-info">
          <h3>Additional Information</h3>
          <div className="form-group">
            <label htmlFor="references">Professional References</label>
            <textarea 
              id="references" 
              name="references" 
              value={formData.references} 
              onChange={handleChange} 
              placeholder="Name, relationship, contact information"
              rows="3"
            />
          </div>

          <div className="form-group">
            <label htmlFor="aboutYou">Tell us about yourself and why you'd be a great fit*</label>
            <textarea 
              id="aboutYou" 
              name="aboutYou" 
              value={formData.aboutYou} 
              onChange={handleChange} 
              required 
              rows="5"
            />
          </div>
        </div>

        <div className="form-footer">
          <p className="required-note">* indicates required field</p>
          <button type="submit" className="submit-btn">Submit Application</button>
          <p className="disclaimer">
            By submitting this application, you agree to our privacy policy. We'll contact you 
            regarding your application. Your information will not be used for any other purpose.
          </p>
        </div>
      </form>
    </div>
  );
};

export default DecoratorApplication;