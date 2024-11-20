import React from "react";
import { ChevronDown } from "./ChevronDown";
import { Size20 } from "./Size20";
import frame2 from "./frame-2.svg";
import frame3 from "./frame-3.svg";
import frame4 from "./frame-4.svg";
import frame from "./frame.svg";
import image from "./image.svg";
import "./style.css";

export const ConcertDetails = () => {
  return (
    <div className="concert-details">
      <div className="div">
        <div className="overlap">
          <div className="text-wrapper">Concerts in Canada</div>

          <div className="overlap-group">
            <div className="text-wrapper-2">City or Postal Code</div>

            <img className="frame" alt="Frame" src={frame} />
          </div>

          <div className="overlap-2">
            <Size20 className="chevron-down" color="white" />
            <div className="text-wrapper-3">All Dates</div>

            <img className="img" alt="Frame" src={image} />
          </div>

          <div className="group">
            <div className="overlap-3">
              <div className="overlap-group-2">
                <div className="text-wrapper-4">Mon</div>

                <div className="text-wrapper-5">Scotia Bank Arena</div>
              </div>

              <div className="overlap-4">
                <div className="text-wrapper-6">Toronto, ON</div>

                <div className="text-wrapper-7">19:00</div>
              </div>

              <div className="NOV">
                NOV
                <br />8
              </div>

              <div className="overlap-5">
                <div className="rectangle" />

                <div className="text-wrapper-8">BOOK NOW</div>

                <ChevronDown className="chevron-down-instance" />
              </div>
            </div>
          </div>

          <div className="overlap-wrapper">
            <div className="overlap-3">
              <div className="overlap-group-2">
                <div className="text-wrapper-4">Mon</div>

                <div className="text-wrapper-5">Scotia Bank Arena</div>
              </div>

              <div className="overlap-4">
                <div className="text-wrapper-6">Toronto, ON</div>

                <div className="text-wrapper-7">19:00</div>
              </div>

              <div className="NOV">
                NOV
                <br />8
              </div>

              <div className="overlap-group-3">
                <div className="text-wrapper-8">BOOK NOW</div>

                <ChevronDown className="chevron-down-instance" />
              </div>
            </div>
          </div>

          <div className="overlap-group-wrapper">
            <div className="overlap-3">
              <div className="overlap-group-2">
                <div className="text-wrapper-4">Mon</div>

                <div className="text-wrapper-5">Scotia Bank Arena</div>
              </div>

              <div className="overlap-4">
                <div className="text-wrapper-6">Toronto, ON</div>

                <div className="text-wrapper-7">19:00</div>
              </div>

              <div className="NOV">
                NOV
                <br />8
              </div>

              <div className="overlap-group-3">
                <div className="text-wrapper-8">BOOK NOW</div>

                <ChevronDown className="chevron-down-instance" />
              </div>
            </div>
          </div>

          <div className="div-wrapper">
            <div className="overlap-3">
              <div className="overlap-group-2">
                <div className="text-wrapper-4">Mon</div>

                <div className="text-wrapper-5">Scotia Bank Arena</div>
              </div>

              <div className="overlap-4">
                <div className="text-wrapper-6">Toronto, ON</div>

                <div className="text-wrapper-7">19:00</div>
              </div>

              <div className="NOV">
                NOV
                <br />8
              </div>

              <div className="overlap-group-3">
                <div className="text-wrapper-8">BOOK NOW</div>

                <ChevronDown className="chevron-down-instance" />
              </div>
            </div>
          </div>

          <div className="group-2">
            <div className="overlap-3">
              <div className="overlap-group-2">
                <div className="text-wrapper-4">Mon</div>

                <div className="text-wrapper-5">Scotia Bank Arena</div>
              </div>

              <div className="overlap-4">
                <div className="text-wrapper-6">Toronto, ON</div>

                <div className="text-wrapper-7">19:00</div>
              </div>

              <div className="NOV">
                NOV
                <br />8
              </div>

              <div className="overlap-group-3">
                <div className="text-wrapper-8">BOOK NOW</div>

                <ChevronDown className="chevron-down-instance" />
              </div>
            </div>
          </div>
        </div>

        <div className="overlap-6">
          <div className="group-3">
            <div className="overlap-group-4">
              <div className="rectangle-2" />

              <div className="text-wrapper-9">LOGO</div>

              <div className="rectangle-3" />

              <div className="text-wrapper-10">Concerts</div>

              <div className="text-wrapper-11">My Tickets</div>

              <div className="text-wrapper-12">Help</div>

              <div className="text-wrapper-13">Log In</div>
            </div>
          </div>

          <div className="rectangle-4" />

          <div className="text-wrapper-14">Artist, Concert Title</div>

          <div className="text-wrapper-15">Jazz</div>

          <div className="description-xxxxxxx">
            Description:
            <br />
            xxxxxxx xx xxxx xxxxx
          </div>

          <div className="text-wrapper-16">Nov 8, 2024</div>

          <img className="frame-2" alt="Frame" src={frame2} />

          <img className="frame-3" alt="Frame" src={frame3} />

          <img className="frame-4" alt="Frame" src={frame4} />
        </div>

        <div className="text-wrapper-17">Ticket results</div>
      </div>
    </div>
  );
};
