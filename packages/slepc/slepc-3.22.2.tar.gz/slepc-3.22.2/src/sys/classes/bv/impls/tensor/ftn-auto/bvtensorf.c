#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* bvtensor.c */
/* Fortran interface file */

/*
* This file was generated automatically by bfort from the C source
* file.  
 */

#ifdef PETSC_USE_POINTER_CONVERSION
#if defined(__cplusplus)
extern "C" { 
#endif 
extern void *PetscToPointer(void*);
extern int PetscFromPointer(void *);
extern void PetscRmPointer(void*);
#if defined(__cplusplus)
} 
#endif 

#else

#define PetscToPointer(a) (a ? *(PetscFortranAddr *)(a) : 0)
#define PetscFromPointer(a) (PetscFortranAddr)(a)
#define PetscRmPointer(a)
#endif

#include "slepcbv.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvtensorbuildfirstcolumn_ BVTENSORBUILDFIRSTCOLUMN
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvtensorbuildfirstcolumn_ bvtensorbuildfirstcolumn
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvtensorcompress_ BVTENSORCOMPRESS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvtensorcompress_ bvtensorcompress
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvtensorgetdegree_ BVTENSORGETDEGREE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvtensorgetdegree_ bvtensorgetdegree
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvtensorgetfactors_ BVTENSORGETFACTORS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvtensorgetfactors_ bvtensorgetfactors
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvtensorrestorefactors_ BVTENSORRESTOREFACTORS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvtensorrestorefactors_ bvtensorrestorefactors
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvcreatetensor_ BVCREATETENSOR
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvcreatetensor_ bvcreatetensor
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  bvtensorbuildfirstcolumn_(BV V,PetscInt *k, int *ierr)
{
CHKFORTRANNULLOBJECT(V);
*ierr = BVTensorBuildFirstColumn(
	(BV)PetscToPointer((V) ),*k);
}
SLEPC_EXTERN void  bvtensorcompress_(BV V,PetscInt *newc, int *ierr)
{
CHKFORTRANNULLOBJECT(V);
*ierr = BVTensorCompress(
	(BV)PetscToPointer((V) ),*newc);
}
SLEPC_EXTERN void  bvtensorgetdegree_(BV bv,PetscInt *d, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
CHKFORTRANNULLINTEGER(d);
*ierr = BVTensorGetDegree(
	(BV)PetscToPointer((bv) ),d);
}
SLEPC_EXTERN void  bvtensorgetfactors_(BV V,BV *U,Mat *S, int *ierr)
{
CHKFORTRANNULLOBJECT(V);
PetscBool U_null = !*(void**) U ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(U);
PetscBool S_null = !*(void**) S ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(S);
*ierr = BVTensorGetFactors(
	(BV)PetscToPointer((V) ),U,S);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! U_null && !*(void**) U) * (void **) U = (void *)-2;
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! S_null && !*(void**) S) * (void **) S = (void *)-2;
}
SLEPC_EXTERN void  bvtensorrestorefactors_(BV V,BV *U,Mat *S, int *ierr)
{
CHKFORTRANNULLOBJECT(V);
PetscBool U_null = !*(void**) U ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(U);
PetscBool S_null = !*(void**) S ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(S);
*ierr = BVTensorRestoreFactors(
	(BV)PetscToPointer((V) ),U,S);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! U_null && !*(void**) U) * (void **) U = (void *)-2;
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! S_null && !*(void**) S) * (void **) S = (void *)-2;
}
SLEPC_EXTERN void  bvcreatetensor_(BV U,PetscInt *d,BV *V, int *ierr)
{
CHKFORTRANNULLOBJECT(U);
PetscBool V_null = !*(void**) V ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(V);
*ierr = BVCreateTensor(
	(BV)PetscToPointer((U) ),*d,V);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! V_null && !*(void**) V) * (void **) V = (void *)-2;
}
#if defined(__cplusplus)
}
#endif
