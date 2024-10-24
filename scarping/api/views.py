import requests
import locale
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from datetime import datetime

locale.setlocale(locale.LC_ALL, 'tr_TR.UTF-8')

def format_amount(amount):
    return locale.format_string('%.2f', amount / 100, grouping=True)

# class CarRentalViewSet(viewsets.ViewSet):

#     @action(detail=False, methods=['post'])
#     def search(self, request):
#         place_id = request.data.get("place_id")  
#         location_url = f"https://maps.cms.yolcu360.com/api/maps/geocode?placeId={place_id}"
#         location_response = requests.get(location_url)

#         location_data = location_response.json()
#         lat = location_data.get("lat")
#         lng = location_data.get("lng")
#         print(lat, lng)
        
#         payload = {
#             "checkInDateTime": request.data.get("checkInDateTime"),
#             "checkOutDateTime": request.data.get("checkOutDateTime"),
#             "age": request.data.get("age"),
#             "checkInLocation": {
#                 "lat": lat,
#                 "lon": lng
#             },
#             "checkOutLocation": {
#                 "lat": lat,
#                 "lon": lng
#             },
#             "country": "TR",
#             "currency": "TRY",
#             "language": "tr",
#             "organizationId": 6836,
#             "paymentType": "creditCard",
#             "period": "daily"
#         }

#         headers = {
#             "Content-Type": "application/json",
#             "accept": "application/json",
#             "accept-language": "tr"
#         }

#         url = "https://api2.yolcu360.com/api/v1/search-api/search/point/"
#         response = requests.post(url, json=payload, headers=headers)

#         if response.status_code == 200:
#             data = response.json()
#             results = data.get('results', [])
#             formatted_results = []

            
#             filters = {
#                 "brand": request.query_params.get("brand"),
#                 "model": request.query_params.get("model"),
#                 "car_class": request.query_params.get("car_class"),
#                 "fuel": request.query_params.get("fuel"),
#                 "seat_count": request.query_params.get("seat_count"),
#                 "segment": request.query_params.get("segment"),
#                 "transmission": request.query_params.get("transmission"),
#                 "vendor": request.query_params.get("vendor")
#             }

#             for car_data in results:
#                 car_details = car_data.get('details', {}).get('car', {})
#                 pricing = car_details.get('pricing', {}).get('display', {}).get('fee', {})
#                 period = car_data.get('period', {})

#                 formatted_car_data = {
#                     "brand": car_details.get('brand', {}).get('name', ''),
#                     "model": car_details.get('model', {}).get('name', ''),
#                     "car_class": car_details.get('class', {}).get('name', ''),
#                     "fuel": car_details.get('fuel', {}).get('name', ''),
#                     "seat_count": car_details.get('seatCount', 0),
#                     "segment": car_details.get('segment', {}).get('name', ''),
#                     "transmission": car_details.get('transmission', {}).get('name', ''),
#                     "vendor": car_details.get('vendor', {}).get('displayName', ''),
#                     "check_in_datetime": car_details.get('appointment', {}).get('checkInDateTime'),
#                     "check_in_office": car_details.get('appointment', {}).get('checkInOffice', {}).get('address', {}).get('adm1', ''),
#                     "check_out_datetime": car_details.get('appointment', {}).get('checkOutDateTime'),
#                     "check_out_office": car_details.get('appointment', {}).get('checkOutOffice', {}).get('address', {}).get('adm1', ''),
#                     "period_amount": period.get('amount', 0),
#                     "display_fee_amount": format_amount(pricing.get('amount', {}).get('amount', 0))
#                 }

#                 if all([
#                     filters.get("brand") is None or formatted_car_data["brand"] == filters["brand"],
#                     filters.get("model") is None or formatted_car_data["model"] == filters["model"],
#                     filters.get("car_class") is None or formatted_car_data["car_class"] == filters["car_class"],
#                     filters.get("fuel") is None or formatted_car_data["fuel"] == filters["fuel"],
#                     filters.get("seat_count") is None or formatted_car_data["seat_count"] == int(filters["seat_count"]),
#                     filters.get("segment") is None or formatted_car_data["segment"] == filters["segment"],
#                     filters.get("transmission") is None or formatted_car_data["transmission"] == filters["transmission"],
#                     filters.get("vendor") is None or formatted_car_data["vendor"] == filters["vendor"]
#                 ]):
#                     formatted_results.append(formatted_car_data)

#             return Response({"results": formatted_results}, status=status.HTTP_200_OK)
#         else:
#             return Response({"error": response.text}, status=response.status_code)
# class CarRentalViewSet(viewsets.ViewSet):

#     @action(detail=False, methods=['post'])
#     def search(self, request):
#         place_id = request.data.get("place_id")
#         if not place_id:
#           return Response({"error": "place_id is required"}, status=status.HTTP_400_BAD_REQUEST)
#         location_url = f"https://maps.cms.yolcu360.com/api/maps/geocode?placeId={place_id}"
#         location_response = requests.get(location_url)

#         if location_response.status_code != 200:
#             return Response({"error": "Location not found"}, status=status.HTTP_404_NOT_FOUND)

#         location_data = location_response.json()
#         lat = location_data.get("lat")
#         lng = location_data.get("lng")

#         payload = {
#             "checkInDateTime": request.data.get("checkInDateTime"),
#             "checkOutDateTime": request.data.get("checkOutDateTime"),
#             "age": request.data.get("age"),
#             "checkInLocation": {
#                 "lat": lat,
#                 "lon": lng
#             },
#             "checkOutLocation": {
#                 "lat": lat,
#                 "lon": lng
#             },
#             "country": "TR",
#             "currency": "TRY",
#             "language": "tr",
#             "organizationId": 6836,
#             "paymentType": "creditCard",
#             "period": "daily"
#         }

#         headers = {
#             "Content-Type": "application/json",
#             "accept": "application/json",
#             "accept-language": "tr"
#         }

#         url = "https://api2.yolcu360.com/api/v1/search-api/search/point/"
#         response = requests.post(url, json=payload, headers=headers)

#         if response.status_code == 200:
#             data = response.json()
#             results = data.get('results', [])
#             formatted_results = []

           
#             for car_data in results:
#                 car_details = car_data.get('details', {}).get('car', {})
#                 pricing = car_data.get('pricing', {}).get('display', {}).get('fee', {}).get('amount', {})
#                 period = car_data.get('period', {})

#                 formatted_car_data = {
#                     "brand": car_details.get('brand', {}).get('name', ''),
#                     "model": car_details.get('model', {}).get('name', ''),
#                     "car_class": car_details.get('class', {}).get('name', ''),
#                     "fuel": car_details.get('fuel', {}).get('name', ''),
#                     "seat_count": car_details.get('seatCount', 0),
#                     "segment": car_details.get('segment', {}).get('name', ''),
#                     "transmission": car_details.get('transmission', {}).get('name', ''),
#                     "vendor": car_details.get('vendor', {}).get('displayName', ''),
#                     "check_in_datetime": car_details.get('appointment', {}).get('checkInDateTime'),
#                     "check_in_office": car_details.get('appointment', {}).get('checkInOffice', {}).get('address', {}).get('adm1', ''),
#                     "check_out_datetime": car_details.get('appointment', {}).get('checkOutDateTime'),
#                     "check_out_office": car_details.get('appointment', {}).get('checkOutOffice', {}).get('address', {}).get('adm1', ''),
#                     "period_amount": period.get('amount', 0),
#                     "display_fee_amount": format_amount(pricing.get('amount', {}))
#                 }

#                 formatted_results.append(formatted_car_data)

#             request.session['car_results'] = formatted_results
            
#             return Response({"results": formatted_results}, status=status.HTTP_200_OK)
#         else:
#             return Response({"error": response.text}, status=response.status_code)

#     @action(detail=False, methods=['get'])
#     def filter(self, request):
#      all_results = request.session.get('car_results', [])

#      filters = {
#         "brand": request.query_params.get("brand"),
#         "model": request.query_params.get("model"),
#         "car_class": request.query_params.get("car_class"),
#         "fuel": request.query_params.get("fuel"),
#         "seat_count": request.query_params.get("seat_count"),
#         "segment": request.query_params.get("segment"),
#         "transmission": request.query_params.get("transmission"),
#         "vendor": request.query_params.get("vendor")
#     }

#      filtered_results = []
    
#      for formatted_car_data in all_results:
#         if all([
#             filters.get("brand") is None or formatted_car_data["brand"] == filters["brand"],
#             filters.get("model") is None or formatted_car_data["model"] == filters["model"],
#             filters.get("car_class") is None or formatted_car_data["car_class"] == filters["car_class"],
#             filters.get("fuel") is None or formatted_car_data["fuel"] == filters["fuel"],
#             filters.get("seat_count") is None or formatted_car_data["seat_count"] == int(filters["seat_count"]),
#             filters.get("segment") is None or formatted_car_data["segment"] == filters["segment"],
#             filters.get("transmission") is None or formatted_car_data["transmission"] == filters["transmission"],
#             filters.get("vendor") is None or formatted_car_data["vendor"] == filters["vendor"]
#         ]):
#             filtered_results.append(formatted_car_data)

#      return Response({"results": filtered_results}, status=status.HTTP_200_OK)


class AutoComplete(viewsets.ViewSet):

    @action(detail=False, methods=['get'])
    def autocomplete(self, request):
        input_text = request.query_params.get("input")
        if not input_text:
            return Response({"error": "Input verisi gereklidir."}, status=status.HTTP_400_BAD_REQUEST)

        url = f"https://maps.cms.yolcu360.com/api/maps/autocomplete?language=tr&input={input_text}&locationbias=circle:100000@40.731647,31.589813"
        
        try:
            response = requests.get(url)
            
            
            if response.history:
                for resp in response.history:
                    print(f"Redirected from: {resp.url} with status code: {resp.status_code}")
                print(f"Final destination: {response.url}")
                
                response = requests.get(response.url)
            
            if response.status_code == 200:
                suggestions = response.json().get('predictions', [])
                formatted_suggestions = [
                    {
                        "place_id": suggestion.get("place_id"),
                        "description": suggestion.get("description"),
                        "matched_substring": suggestion.get("matched_substring")
                    } for suggestion in suggestions
                ]
                return Response({"suggestions": formatted_suggestions}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Otomatik tamamlama bilgisi alınamadı."}, status=status.HTTP_400_BAD_REQUEST)

        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CarRentalEnViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['post'])
    def search(self, request):
        pick_up_date = request.data.get("pickUpDate")
        drop_off_date = request.data.get("dropOffDate")
        pick_up_location = request.data.get("pickUpLocation")
        drop_off_location = request.data.get("dropOffLocation")
        pick_up_time = request.data.get("pickUpTime")
        drop_off_time = request.data.get("dropOffTime")
        trip = request.data.get("trip", "domestic")
        
        pagination = request.data.get("pagination", {"page": 1, "limit": 10}) 
        page = pagination.get("page", 1)
        limit = pagination.get("limit", 10)

        if not all([pick_up_date, drop_off_date, pick_up_location, drop_off_location, pick_up_time, drop_off_time]):
            return Response({"error": "All required fields must be provided."}, status=status.HTTP_400_BAD_REQUEST)
        

        
        all_reservations = []  
        
        while True:
           
            payload = {
                "pickUpDate": pick_up_date,
                "dropOffDate": drop_off_date,
                "pickUpLocation": pick_up_location,
                "dropOffLocation": drop_off_location,
                "pickUpTime": pick_up_time,
                "dropOffTime": drop_off_time,
                "trip":trip,
                "pagination": {
                    "page": page,
                    "limit": limit
                }
            }

            url = "https://cr-search.enuygun.com/api/v1/search"
            response = requests.post(url, json=payload)
            
            if response.status_code == 200:
                data = response.json()
                reservations = data.get('data', {}).get('reservations', [])

                if not reservations:
                    break  

                all_reservations.extend(reservations)
                page += 1 
            else:
                return Response({"error": response.text}, status=response.status_code)

        if not all_reservations:
            return Response({"error": "No cars found matching the criteria."}, status=status.HTTP_404_NOT_FOUND)

        formatted_results = []
      
        
        
        for reservation in all_reservations:
            vehicle = reservation.get("vehicle", {})
            price = reservation.get("price", {})
            location = reservation.get("location", {})
            
            formatted_car_data = {
                "office": location.get('slug', ''),
                "pickup_date": pick_up_date,
                "dropoff_date": drop_off_date,
                "car_class": vehicle.get('class', ''),
                "company": reservation.get('company', {}).get('name', ''),
                "brand": vehicle.get('brand', ''),
                "model": vehicle.get('name', ''),
                "transmission": vehicle.get('transmission', ''),
                "fuel": vehicle.get('fuel', ''),
                "total_price": price.get('totalPrice', 0),
                "days": reservation.get('days',0)
            }
            
            formatted_results.append(formatted_car_data)

        return Response({
            "results": formatted_results
        }, status=status.HTTP_200_OK)
class CarRentalViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['post'])
    def search(self, request):
        service = request.data.get("service")  
        if service not in ["yolcu360", "enuygun"]:
            return Response({"error": "Invalid service specified."}, status=status.HTTP_400_BAD_REQUEST)

        if service == "yolcu360":
            place_id = request.data.get("place_id")
            if not place_id:
                return Response({"error": "place_id is required"}, status=status.HTTP_400_BAD_REQUEST)

            location_url = f"https://maps.cms.yolcu360.com/api/maps/geocode?placeId={place_id}"
            location_response = requests.get(location_url)

            if location_response.status_code != 200:
                return Response({"error": "Location not found"}, status=status.HTTP_404_NOT_FOUND)

            location_data = location_response.json()
            lat = location_data.get("lat")
            lng = location_data.get("lng")
        
            check_in_time = request.data.get("checkInDateTime")
            check_out_time = request.data.get("checkOutDateTime")

            payload = {
                "checkInDateTime": check_in_time,
                "checkOutDateTime": check_out_time,
                "age": request.data.get("age"),
                "checkInLocation": {
                    "lat": lat,
                    "lon": lng
                },
                "checkOutLocation": {
                    "lat": lat,
                    "lon": lng
                },
                "country": "TR",
                "currency": "TRY",
                "language": "tr",
                "organizationId": 6836,
                "paymentType": "creditCard",
                "period": "daily"
            }

            url = "https://api2.yolcu360.com/api/v1/search-api/search/point/"
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                data = response.json()
                results = data.get('results') or []
                print(len(results))
                formatted_results = []

                for car_data in results:
                    car_details = car_data.get('details', {}).get('car', {})
                    pricing = car_data.get('pricing', {}).get('display', {}).get('fee', {}).get('amount', {})
                    period = car_data.get('period', {})

                    formatted_car_data = {
                        "Ofis": car_details.get('appointment', {}).get('checkInOffice', {}).get('address', {}).get('adm1', ''),
                        "Başlangıç_tarihi": car_details.get('appointment', {}).get('checkInDateTime'),
                        "Bitiş_Tarihi": car_details.get('appointment', {}).get('checkOutDateTime'),
                        "Araç_Grubu": car_details.get('class', {}).get('name', ''),
                        "Firma": car_details.get('vendor', {}).get('displayName', ''),
                        "Broker": "Yolcu360",
                        "Marka": car_details.get('brand', {}).get('name', ''),
                        "Model": car_details.get('model', {}).get('name', ''),
                        "Vites": car_details.get('transmission', {}).get('name', ''),
                        "Yakıt": car_details.get('fuel', {}).get('name', ''),
                        "Koltuk_Sayısı": car_details.get('seatCount', 0),
                        "Fiyat": format_amount(pricing.get('amount', {})),
                        "Gün": period.get('amount', 0),
                    }

                    formatted_results.append(formatted_car_data)
                    
                
                filters = request.data.get("filters", {})  
                filtered_results = []

                for formatted_car_data in formatted_results:  
                    if filters.get("brand") and formatted_car_data["Marka"] != filters["brand"]:
                        continue
                    if filters.get("model") and formatted_car_data["Model"] != filters["model"]:
                        continue
                    if filters.get("car_class") and formatted_car_data["Araç_Grubu"] != filters["car_class"]:
                        continue
                    if filters.get("fuel") and formatted_car_data["Yakıt"] != filters["fuel"]:
                        continue
                    if filters.get("transmission") and formatted_car_data["Vites"] != filters["transmission"]:
                        continue
                    if filters.get("vendor") and formatted_car_data["Firma"] != filters["vendor"]:
                        continue

                    filtered_results.append(formatted_car_data)
                    print(len(filtered_results))

                return Response({"results": filtered_results}, status=status.HTTP_200_OK)
            else:
                return Response({"error": response.text}, status=response.status_code)

        elif service == "enuygun":
            pick_up_date = request.data.get("pickUpDate")
            drop_off_date = request.data.get("dropOffDate")
            pick_up_location = request.data.get("pickUpLocation")
            drop_off_location = request.data.get("dropOffLocation")
            pick_up_time = request.data.get("pickUpTime")
            drop_off_time = request.data.get("dropOffTime")
            trip = request.data.get("trip", "domestic")
            pagination = request.data.get("pagination", {"page": 1, "limit": 10})
            page = pagination.get("page", 1)
            limit = pagination.get("limit", 10)

            if not all([pick_up_date, drop_off_date, pick_up_location, drop_off_location, pick_up_time, drop_off_time]):
                return Response({"error": "All required fields must be provided."}, status=status.HTTP_400_BAD_REQUEST)

            all_reservations = []

            while True:
                payload = {
                    "pickUpDate": pick_up_date,
                    "dropOffDate": drop_off_date,
                    "pickUpLocation": pick_up_location,
                    "dropOffLocation": drop_off_location,
                    "pickUpTime": pick_up_time,
                    "dropOffTime": drop_off_time,
                    "trip": trip,
                    "pagination": {
                        "page": page,
                        "limit": limit
                    }
                }

                url = "https://cr-search.enuygun.com/api/v1/search"
                response = requests.post(url, json=payload)

                if response.status_code == 200:
                    data = response.json()
                    reservations = data.get('data', {}).get('reservations', [])

                    if not reservations:
                        break

                    all_reservations.extend(reservations)
                    page += 1
                else:
                    return Response({"error": response.text}, status=response.status_code)

            if not all_reservations:
                return Response({"error": "No cars found matching the criteria."}, status=status.HTTP_404_NOT_FOUND)

            formatted_results = []

            for reservation in all_reservations:
                vehicle = reservation.get("vehicle", {})
                price = reservation.get("price", {})
                location = reservation.get("location", {})

                formatted_car_data = {
                    "Ofis": location.get('slug', ''),
                    "Başlangıç_tarihi": pick_up_date,
                    "Bitiş_Tarihi": drop_off_date,
                    "Araç_Grubu": vehicle.get('class', ''),
                    "Firma": reservation.get('company', {}).get('name', ''),
                    "Broker":"EnUygun",
                    "Marka": vehicle.get('brand', ''),
                    "Model": vehicle.get('name', ''),
                    "Vites": vehicle.get('transmission', ''),
                    "Yakıt": vehicle.get('fuel', ''),
                    "Fiyat": price.get('totalPrice', 0),
                    "Gün": reservation.get('days', 0),
                    
                }

                formatted_results.append(formatted_car_data)

            
            filters = request.data.get("filters", {}) 
            filtered_results = []

            for formatted_car_data in formatted_results: 
                if filters.get("brand") and formatted_car_data["Marka"] != filters["brand"]:
                    continue
                if filters.get("model") and formatted_car_data["Model"] != filters["model"]:
                    continue
                if filters.get("car_class") and formatted_car_data["Araç_Grubu"] != filters["car_class"]:
                    continue
                if filters.get("fuel") and formatted_car_data["Yakıt"] != filters["fuel"]:
                    continue
                if filters.get("transmission") and formatted_car_data["Vites"] != filters["transmission"]:
                    continue
                if filters.get("vendor") and formatted_car_data["Firma"] != filters["vendor"]:
                    continue

                filtered_results.append(formatted_car_data)

            return Response({"results": filtered_results}, status=status.HTTP_200_OK)

    
  
from rest_framework.response import Response
from rest_framework import status
import requests

class CarFilterViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['post'])
    def search(self, request):
        service = request.data.get("service")  
        if service not in ["yolcu360", "enuygun"]:
            return Response({"error": "Invalid service specified."}, status=status.HTTP_400_BAD_REQUEST)
        
        if service == "yolcu360":
            place_id = request.data.get("place_id")
            if not place_id:
                return Response({"error": "place_id is required"}, status=status.HTTP_400_BAD_REQUEST)
            
            location_url = f"https://maps.cms.yolcu360.com/api/maps/geocode?placeId={place_id}"
            location_response = requests.get(location_url)
            if location_response.status_code != 200:
                return Response({"error": "Location not found"}, status=status.HTTP_404_NOT_FOUND)
            
            location_data = location_response.json()
            lat = location_data.get("lat")
            lng = location_data.get("lng")
            check_in_time = request.data.get("checkInDateTime")
            check_out_time = request.data.get("checkOutDateTime")
            
            payload = {
                "checkInDateTime": check_in_time,
                "checkOutDateTime": check_out_time,
                "age": request.data.get("age"),
                "checkInLocation": {
                    "lat": lat,
                    "lon": lng
                },
                "checkOutLocation": {
                    "lat": lat,
                    "lon": lng
                },
                "country": "TR",
                "currency": "TRY",
                "language": "tr",
                "organizationId": 6836,
                "paymentType": "creditCard",
                "period": "daily"
            } 
            
            url = "https://api2.yolcu360.com/api/v1/search-api/search/point/"
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                results = data.get('results') or []       
                
                available_brands = {}
                available_models = {}
                available_car_classes = {}
                available_fuels = {}
                available_transmissions = {}
                available_vendors = {}

               
                filter_brands = request.data.get("filters", {}).get("brands", [])
                filter_brands_set = set(filter_brands) if filter_brands else None

                for car_data in results:
                    car_details = car_data.get('details', {}).get('car', {})
                    
                    brand_name = car_details.get('brand', {}).get('name', '')
                    if brand_name and (filter_brands_set is None or brand_name in filter_brands_set):
                        available_brands[brand_name] = available_brands.get(brand_name, 0) + 1

                        model_name = car_details.get('model', {}).get('name', '')
                        if model_name:
                            available_models[model_name] = available_models.get(model_name, 0) + 1

                        car_class_name = car_details.get('class', {}).get('name', '')
                        if car_class_name:
                            available_car_classes[car_class_name] = available_car_classes.get(car_class_name, 0) + 1

                        fuel_name = car_details.get('fuel', {}).get('name', '')
                        if fuel_name:
                            available_fuels[fuel_name] = available_fuels.get(fuel_name, 0) + 1

                        transmission_name = car_details.get('transmission', {}).get('name', '')
                        if transmission_name:
                            available_transmissions[transmission_name] = available_transmissions.get(transmission_name, 0) + 1

                        vendor_name = car_details.get('vendor', {}).get('displayName', '')
                        if vendor_name:
                            available_vendors[vendor_name] = available_vendors.get(vendor_name, 0) + 1

                filters = {
                    "brands": available_brands,
                    "models": available_models,  
                    "car_classes": available_car_classes,  
                    "fuels": available_fuels,  
                    "transmissions": available_transmissions,  
                    "vendors": available_vendors,  
                }
                
                return Response({"filters": filters}, status=status.HTTP_200_OK)
            else:
                return Response({"error": response.text}, status=response.status_code)
