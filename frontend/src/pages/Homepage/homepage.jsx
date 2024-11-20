import React from "react";
import "../style.css";
import frame2 from "../assets/frame-2.svg";
import frame3 from "../assets/frame-3.svg";
import frame from "../assets/frame.svg";
import image from "../assets/image.svg";
import line14 from "../assets/line-14.svg";
import line15 from "../assets/line-15.svg";
import searchSvgrepoCom1 from "../assets/search-svgrepo-com-1.svg";

export const HomePage = () => {
  return (
    <div className="home-page">
      <div className="div">
        <div className="group">
          <div className="overlap-group">
            <div className="text-wrapper">LOGO</div>
            <div className="text-wrapper-2">Concerts</div>
            <div className="text-wrapper-3">My Tickets</div>
            <div className="text-wrapper-4">Help</div>
            <div className="text-wrapper-5">Log In</div>
          </div>
        </div>
        <div className="overlap">
          <img className="frame" alt="Frame" src={frame} />
        </div>
        <div className="frame-wrapper">
          <img className="img" alt="Frame" src={frame2} />
        </div>
        <div className="img-wrapper">
          <img className="frame-2" alt="Frame" src={image} />
        </div>
        <div className="overlap-2">
          <img className="frame-2" alt="Frame" src={frame3} />
        </div>
        <div className="text-wrapper-6">Featured Concerts</div>
        <div className="overlap-3">
          <div className="rectangle" />
          <div className="text-wrapper-7">Artist/Group</div>
          <div className="text-wrapper-8">Date</div>
          <div className="text-wrapper-9">Location</div>
          <div className="starting-price-XX-XX">
            Starting Price
            <br />
            $XX.XX
          </div>
        </div>
        <div className="overlap-4">
          <div className="rectangle" />
          <div className="text-wrapper-10">Artist/Group</div>
          <div className="text-wrapper-11">Date</div>
          <div className="text-wrapper-12">Location</div>
          <div className="starting-price-XX-XX-2">
            Starting Price
            <br />
            $XX.XX
          </div>
        </div>
        <div className="overlap-5">
          <div className="rectangle" />
          <div className="text-wrapper-7">Artist/Group</div>
          <div className="text-wrapper-13">Date</div>
          <div className="text-wrapper-14">Location</div>
          <div className="starting-price-XX-XX">
            Starting Price
            <br />
            $XX.XX
          </div>
        </div>
        <div className="overlap-6">
          <div className="rectangle" />
          <div className="text-wrapper-10">Artist/Group</div>
          <div className="text-wrapper-11">Date</div>
          <div className="text-wrapper-12">Location</div>
          <div className="starting-price-XX-XX-3">
            Starting Price
            <br />
            $XX.XX
          </div>
        </div>
        <div className="overlap-wrapper">
          <div className="overlap-7">
            <p className="p">Search by artist or venue</p>
            <img
              className="search-svgrepo-com"
              alt="Search icon"
              src={searchSvgrepoCom1}
            />
            <img className="line" alt="Line" src={line14} />
            <img className="line-2" alt="Line" src={line15} />
            <div className="text-wrapper-15">All Dates</div>
            <div className="text-wrapper-16">City or Postal Code</div>
          </div>
        </div>
      </div>
    </div>
  );
};